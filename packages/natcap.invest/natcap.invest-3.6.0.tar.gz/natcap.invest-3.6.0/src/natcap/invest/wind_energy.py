"""InVEST Wind Energy model."""
from __future__ import absolute_import

import logging
import os
import csv
import shutil
import tempfile
import math

import numpy as np
import pandas
from scipy import integrate
# required for py2exe to build
from scipy.sparse.csgraph import _validation

import shapely.wkb
import shapely.wkt
import shapely.ops
import shapely.prepared
from shapely import speedups

from osgeo import gdal
from osgeo import ogr
from osgeo import osr

import pygeoprocessing
from . import validation
from . import utils

LOGGER = logging.getLogger('natcap.invest.wind_energy')

speedups.enable()

# The _SCALE_KEY is used in getting the right wind energy arguments that are
# dependent on the hub height.
_SCALE_KEY = 'LAM'

# The str name for the shape field. So far this is a default from the
# text file given by CK. I guess we could search for the 'K' if needed.
_SHAPE_KEY = 'K'

# Set the raster nodata value and data type to use throughout the model
_TARGET_NODATA = -64329.0
_TARGET_DATA_TYPE = gdal.GDT_Float32

# The harvested energy is on a per year basis
_NUM_DAYS = 365

# Constant used in getting Scale value at hub height from reference height
# values. See equation 3 in the users guide.
_ALPHA = 0.11

# Field name to be added to the land point shapefile
_LAND_TO_GRID_FIELD = 'L2G'


def execute(args):
    """Wind Energy.

    This module handles the execution of the wind energy model
    given the following dictionary:

    Args:
        workspace_dir (str): a path to the output workspace folder (required)
        wind_data_path (str): path to a CSV file with the following header:
            ['LONG','LATI','LAM', 'K', 'REF']. Each following row is a location
            with at least the Longitude, Latitude, Scale ('LAM'),
            Shape ('K'), and reference height ('REF') at which the data was
            collected (required)
        aoi_vector_path (str): a path to an OGR polygon vector that is
            projected in linear units of meters. The polygon specifies the
            area of interest for the wind data points. If limiting the wind
            farm bins by distance, then the aoi should also cover a portion
            of the land polygon that is of interest (optional for biophysical
            and no distance masking, required for biophysical and distance
            masking, required for valuation)
        bathymetry_path (str): a path to a GDAL raster that has the depth
            values of the area of interest (required)
        land_polygon_vector_path (str): a path to an OGR polygon vector that
            provides a coastline for determining distances from wind farm bins.
            Enabled by AOI and required if wanting to mask by distances or run
            valuation
        global_wind_parameters_path (str): a float for the average distance
            in kilometers from a grid connection point to a land connection
            point (required for valuation if grid connection points are not
            provided)
        suffix (str): a str to append to the end of the output files
            (optional)
        turbine_parameters_path (str): a path to a CSV file that holds the
            turbines biophysical parameters as well as valuation parameters
            (required)
        number_of_turbines (int): an integer value for the number of machines
            for the wind farm (required for valuation)
        min_depth (float): a float value for the minimum depth for offshore
            wind farm installation (meters) (required)
        max_depth (float): a float value for the maximum depth for offshore
            wind farm installation (meters) (required)
        min_distance (float): a float value for the minimum distance from shore
            for offshore wind farm installation (meters) The land polygon must
            be selected for this input to be active (optional, required for
            valuation)
        max_distance (float): a float value for the maximum distance from shore
            for offshore wind farm installation (meters) The land polygon must
            be selected for this input to be active (optional, required for
            valuation)
        valuation_container (boolean): Indicates whether model includes
            valuation
        foundation_cost (float): a float representing how much the foundation
            will cost for the specific type of turbine (required for valuation)
        discount_rate (float): a float value for the discount rate (required
            for valuation)
        grid_points_path (str): a path to a CSV file that specifies the
            landing and grid point locations (optional)
        avg_grid_distance (float): a float for the average distance in
            kilometers from a grid connection point to a land connection point
            (required for valuation if grid connection points are not provided)
        price_table (boolean): a bool indicating whether to use the wind energy
            price table or not (required)
        wind_schedule (str): a path to a CSV file for the yearly prices of
            wind energy for the lifespan of the farm (required if 'price_table'
            is true)
        wind_price (float): a float for the wind energy price at year 0
            (required if price_table is false)
        rate_change (float): a float as a percent for the annual rate of change
            in the price of wind energy. (required if price_table is false)

    Example Args Dictionary::

        {
            'workspace_dir': 'path/to/workspace_dir',
            'wind_data_path': 'path/to/file',
            'aoi_vector_path': 'path/to/shapefile',
            'bathymetry_path': 'path/to/raster',
            'land_polygon_vector_path': 'path/to/shapefile',
            'global_wind_parameters_path': 'path/to/csv',
            'suffix': '_results',
            'turbine_parameters_path': 'path/to/csv',
            'number_of_turbines': 10,
            'min_depth': 3,
            'max_depth': 60,
            'min_distance': 0,
            'max_distance': 200000,
            'valuation_container': True,
            'foundation_cost': 3.4,
            'discount_rate': 7.0,
            'grid_points_path': 'path/to/csv',
            'avg_grid_distance': 4,
            'price_table': True,
            'wind_schedule': 'path/to/csv',
            'wind_price': 0.4,
            'rate_change': 0.0,
        }

    Returns:
        None

    """

    LOGGER.debug('Starting the Wind Energy Model')

    workspace = args['workspace_dir']
    inter_dir = os.path.join(workspace, 'intermediate')
    out_dir = os.path.join(workspace, 'output')
    utils.make_directories([inter_dir, out_dir])

    # Resample the bathymetry raster if it does not have square pixel size
    try:
        bathy_pixel_size = pygeoprocessing.get_raster_info(
            args['bathymetry_path'])['pixel_size']
        mean_pixel_size, _ = utils.mean_pixel_size_and_area(bathy_pixel_size)
        bathymetry_path = args['bathymetry_path']
    except ValueError:
        LOGGER.debug(
            '%s has pixels that are not square. Resampling the raster to have '
            'square pixels.' % args['bathymetry_path'])
        bathymetry_path = os.path.join(inter_dir, 'bathymetry_resampled.tif')
        # Get the minimum absolute value from the bathymetry pixel size tuple
        mean_pixel_size = np.min(np.absolute(bathy_pixel_size))
        pygeoprocessing.warp_raster(
            args['bathymetry_path'], (mean_pixel_size, -mean_pixel_size),
            bathymetry_path, 'near')

    number_of_turbines = int(args['number_of_turbines'])

    # Append a _ to the suffix if it's not empty and doesn't already have one
    suffix = utils.make_suffix_string(args, 'suffix')

    # Create a list of the biophysical parameters we are looking for from the
    # input csv files
    biophysical_params = [
        'cut_in_wspd', 'cut_out_wspd', 'rated_wspd', 'hub_height',
        'turbine_rated_pwr', 'air_density', 'exponent_power_curve',
        'air_density_coefficient', 'loss_parameter', 'turbines_per_circuit',
        'rotor_diameter', 'rotor_diameter_factor'
    ]

    # Read the biophysical turbine parameters into a dictionary
    bio_turbine_dict = _read_csv_wind_parameters(
        args['turbine_parameters_path'], biophysical_params)

    # Read the biophysical global parameters into a dictionary
    bio_global_params_dict = _read_csv_wind_parameters(
        args['global_wind_parameters_path'], biophysical_params)

    # Combine the turbine and global parameters into one dictionary
    bio_parameters_dict = bio_global_params_dict.copy()
    bio_parameters_dict.update(bio_turbine_dict)

    LOGGER.debug('Biophysical Turbine Parameters: %s', bio_parameters_dict)

    # Check that all the necessary input fields from the CSV files have been
    # collected by comparing the number of dictionary keys to the number of
    # elements in our known list
    missing_biophysical_params = list(
        set(biophysical_params) - set(bio_parameters_dict.keys()))
    if missing_biophysical_params:
        raise ValueError(
            'The following field value(s) are missing from either the Turbine '
            'CSV file or the Global Wind Energy parameters CSV file: %s'
            'Please make sure all the necessary fields are present and '
            'spelled correctly.' % missing_biophysical_params)

    if 'valuation_container' not in args or args['valuation_container'] is False:
        LOGGER.debug('Valuation Not Selected')
    else:
        LOGGER.info(
            'Valuation Selected. Checking required parameters from CSV files.')

        # Create a list of the valuation parameters we are looking for from the
        # input files
        valuation_turbine_params = ['turbine_cost', 'turbine_rated_pwr']
        # Read the biophysical turbine parameters into a dictionary
        val_turbine_dict = _read_csv_wind_parameters(
            args['turbine_parameters_path'], valuation_turbine_params)
        # Check that all the necessary input fields from the CSV file
        missing_turbine_params = list(
            set(valuation_turbine_params) - set(val_turbine_dict.keys()))

        valuation_global_params = [
            'carbon_coefficient', 'time_period', 'infield_cable_cost',
            'infield_cable_length', 'installation_cost',
            'miscellaneous_capex_cost', 'operation_maintenance_cost',
            'decommission_cost', 'ac_dc_distance_break', 'mw_coef_ac',
            'mw_coef_dc', 'cable_coef_ac', 'cable_coef_dc'
        ]
        # Read the biophysical global parameters into a dictionary
        val_global_param_dict = _read_csv_wind_parameters(
            args['global_wind_parameters_path'], valuation_global_params)
        # Check all the necessary input fields from the CSV file
        missing_global_params = list(
            set(valuation_global_params) - set(val_global_param_dict.keys()))

        if missing_turbine_params or missing_global_params:
            raise ValueError(
                'The following field value(s) are missing: \nTurbine CSV file:'
                ' %s. \nGlobal Wind Energy parameters CSV file: %s. \nPlease '
                'make sure all the necessary fields are present and spelled '
                'correctly.' % (missing_turbine_params, missing_global_params))

        # Combine the turbine and global parameters into one dictionary
        val_parameters_dict = val_global_param_dict.copy()
        val_parameters_dict.update(val_turbine_dict)

        # If Price Table provided use that for price of energy, validate inputs
        time = int(val_parameters_dict['time_period'])
        if args["price_table"]:
            wind_price_df = pandas.read_csv(args["wind_schedule"])
            wind_price_df.columns = wind_price_df.columns.str.lower()

            if not pandas.api.types.is_integer_dtype(wind_price_df['year']):
                raise ValueError(
                    "Please make sure that the Year column in the Wind Energy "
                    "Price Table is integer.")

            if not pandas.api.types.is_numeric_dtype(wind_price_df['price']):
                raise ValueError(
                    "Please make sure that the Price column in the Wind Energy"
                    " Price Table is numeric.")

            year_list = wind_price_df['year'].tolist()
            duplicate_years = set(
                [year for year in year_list if year_list.count(year) > 1])
            if duplicate_years:
                raise ValueError(
                    "The following year(s) showed up more than once in the "
                    "Wind Energy Price Table: %s. Please remove the duplicated"
                    " years from the table.", list(duplicate_years))

            year_count = len(wind_price_df['year'])
            if year_count != time + 1:
                raise ValueError(
                    "The 'time' argument in the Global Wind Energy Parameters "
                    "file must equal the number of years provided in the price"
                    " table.")

            # Save the price values into a list where the indices of the list
            # indicate the time steps for the lifespan of the wind farm
            wind_price_df.sort_values('year', inplace=True)
            price_list = wind_price_df['price'].tolist()
        else:
            change_rate = float(args["rate_change"])
            wind_price = float(args["wind_price"])
            # Build up a list of price values where the indices of the list
            # are the time steps for the lifespan of the farm and values
            # are adjusted based on the rate of change
            price_list = []
            for time_step in xrange(time + 1):
                price_list.append(wind_price * (1 + change_rate)**(time_step))

    # Hub Height to use for setting Weibull parameters
    hub_height = int(bio_parameters_dict['hub_height'])

    LOGGER.debug('hub_height : %s', hub_height)

    # Read the wind energy data into a dictionary
    LOGGER.info('Reading in Wind Data into a dictionary')
    wind_data = _read_csv_wind_data(args['wind_data_path'], hub_height)

    if 'grid_points_path' in args:
        if 'aoi_vector_path' not in args:
            raise ValueError(
                'An AOI shapefile is required to clip and reproject the grid '
                'points.')
        grid_points_dict = utils.build_lookup_from_csv(
            args['grid_points_path'], 'id')  # turn all strs to lower-cased
        missing_grid_fields = list({'long', 'lati', 'id', 'type'} - set(
            grid_points_dict.itervalues().next().keys()))
        if missing_grid_fields:
            raise ValueError(
                'The following field value(s) are missing from the Grid '
                'Connection Points csv file: %s.' % missing_grid_fields)

    if 'aoi_vector_path' in args:
        LOGGER.info('AOI Provided')
        aoi_vector_path = args['aoi_vector_path']

        # Clip and project the bathymetry shapefile to AOI
        LOGGER.info('Clip and project bathymetry to AOI')
        bathymetry_proj_raster_path = os.path.join(
            inter_dir, 'bathymetry_projected%s.tif' % suffix)
        _clip_to_projection_with_square_pixels(bathymetry_path, aoi_vector_path,
                                               bathymetry_proj_raster_path)

        # Since an AOI was provided the wind energy points shapefile will need
        # to be clipped and projected. Thus save the construction of the
        # shapefile from dictionary in the intermediate directory. The final
        # projected shapefile will be written to the output directory
        wind_point_vector_path = os.path.join(
            inter_dir, 'wind_energy_points_from_data%s.shp' % suffix)

        # Create point shapefile from wind data
        LOGGER.info('Create point shapefile from wind data')
        # Use the projection from the projected bathymetry as reference
        bathy_projection_wkt = pygeoprocessing.get_raster_info(
            bathymetry_proj_raster_path)['projection']
        _wind_data_to_point_vector(wind_data, 'wind_data',
                                   wind_point_vector_path, bathy_projection_wkt)

        # Clip the wind energy point shapefile to AOI
        LOGGER.info('Clip and project wind points to AOI')
        wind_point_proj_vector_path = os.path.join(
            out_dir, 'wind_energy_points%s.shp' % suffix)
        _clip_vector_by_vector(wind_point_vector_path, aoi_vector_path,
                               wind_point_proj_vector_path)

        # Set the bathymetry and points path to use in the rest of the model.
        # In this case these paths refer to the projected files. This may not
        # be the case if an AOI is not provided
        final_bathy_raster_path = bathymetry_proj_raster_path
        final_wind_point_vector_path = wind_point_proj_vector_path

        # Try to handle the distance inputs and land datasource if they
        # are present
        try:
            min_distance = float(args['min_distance'])
            max_distance = float(args['max_distance'])
            land_polygon_vector_path = args['land_polygon_vector_path']
        except KeyError:
            LOGGER.info('Distance information not provided')
        else:
            # Clip and project the land polygon shapefile to AOI
            LOGGER.info('Clip and project land poly to AOI')
            land_poly_proj_vector_path = os.path.join(
                inter_dir,
                os.path.basename(land_polygon_vector_path).replace(
                    '.shp', '_projected_clipped%s.shp' % suffix))
            _clip_and_reproject_vector(land_polygon_vector_path,
                                       aoi_vector_path,
                                       land_poly_proj_vector_path, inter_dir)

            # Get the cell size to use in new raster outputs from the DEM
            pixel_size = pygeoprocessing.get_raster_info(
                final_bathy_raster_path)['pixel_size']

            # If the distance inputs are present create a mask for the output
            # area that restricts where the wind energy farms can be based
            # on distance
            aoi_raster_path = os.path.join(inter_dir,
                                           'aoi_raster%s.tif' % suffix)

            # Make a raster from AOI using the bathymetry rasters pixel size
            LOGGER.debug('Create Raster From AOI')
            pygeoprocessing.create_raster_from_vector_extents(
                aoi_vector_path, aoi_raster_path, pixel_size,
                gdal.GDT_Byte, _TARGET_NODATA)

            dist_trans_path = os.path.join(inter_dir,
                                           'distance_trans%s.tif' % suffix)
            _create_distance_raster(aoi_raster_path, land_poly_proj_vector_path,
                                    dist_trans_path, inter_dir)

            dist_mask_path = os.path.join(inter_dir,
                                          'distance_mask%s.tif' % suffix)
            _mask_by_distance(dist_trans_path, min_distance, max_distance,
                              _TARGET_NODATA, dist_mask_path)

    else:
        LOGGER.info("AOI argument was not selected")

        # Since no AOI was provided the wind energy points shapefile that is
        # created directly from dictionary will be the final output, so set the
        # path to point to the output folder
        wind_point_vector_path = os.path.join(
            out_dir, 'wind_energy_points%s.shp' % suffix)

        # Create point shapefile from wind data dictionary
        LOGGER.info('Create point shapefile from wind data')
        _wind_data_to_point_vector(wind_data, 'wind_data',
                                   wind_point_vector_path)

        # Set the bathymetry and points path to use in the rest of the model.
        # In this case these paths refer to the unprojected files. This may not
        # be the case if an AOI is provided
        final_wind_point_vector_path = wind_point_vector_path
        final_bathy_raster_path = bathymetry_path

    # Get the min and max depth values from the arguments and set to a negative
    # value indicating below sea level
    min_depth = abs(float(args['min_depth'])) * -1.0
    max_depth = abs(float(args['max_depth'])) * -1.0

    def _depth_op(bath):
        """Determine if a value falls within the range.

        The function takes a value and uses a range to determine if that falls
        within the range.

        Parameters:
            bath (int): a value of either positive or negative
            min_depth (float): a value specifying the lower limit of the
                range. This value is set above
            max_depth (float): a value specifying the upper limit of the
                range. This value is set above
            _TARGET_NODATA (int or float): a nodata value set above

        Returns:
            out_array (np.array): an array where values are _TARGET_NODATA
                if 'bath' does not fall within the range, or 'bath' if it does.

        """
        out_array = np.full(
            bath.shape, _TARGET_NODATA, dtype=np.float32)
        valid_pixels_mask = ((bath >= max_depth) & (bath <= min_depth) &
                             (bath != _TARGET_NODATA))
        out_array[
            valid_pixels_mask] = bath[valid_pixels_mask]
        return out_array

    depth_mask_path = os.path.join(inter_dir, 'depth_mask%s.tif' % suffix)

    # Get the cell size here to use from the DEM. The cell size could either
    # come in a project unprojected format
    pixel_size = pygeoprocessing.get_raster_info(final_bathy_raster_path)[
        'pixel_size']

    # Create a mask for any values that are out of the range of the depth values
    LOGGER.info('Creating Depth Mask')
    pygeoprocessing.raster_calculator([(final_bathy_raster_path, 1)], _depth_op,
                                      depth_mask_path, _TARGET_DATA_TYPE,
                                      _TARGET_NODATA)

    # Weibull probability function to integrate over
    def _calc_weibull_probability(v_speed, k_shape, l_scale):
        """Calculate the Weibull probability function of variable v_speed.

        Parameters:
            v_speed (int or float): a number representing wind speed
            k_shape (float): the shape parameter
            l_scale (float): the scale parameter of the distribution

        Returns:
            a float

        """
        return ((k_shape / l_scale) * (v_speed / l_scale)**
                (k_shape - 1) * (math.exp(-1 * (v_speed / l_scale)**k_shape)))

    # Density wind energy function to integrate over
    def _calc_density_wind_energy(v_speed, k_shape, l_scale):
        """Calculate the probability density function of a Weibull variable.

        Parameters:
            v_speed (int or float): a number representing wind speed
            k_shape (float): the shape parameter
            l_scale (float): the scale parameter of the distribution

        Returns:
            a float

        """
        return ((k_shape / l_scale) * (v_speed / l_scale)**(k_shape - 1) *
                (math.exp(-1 * (v_speed / l_scale)**k_shape))) * v_speed**3

    # Harvested wind energy function to integrate over
    def _calc_harvested_wind_energy(v_speed, k_shape, l_scale):
        """Calculate the harvested wind energy.

        Parameters:
            v_speed (int or float): a number representing wind speed
            k_shape (float): the shape parameter
            l_scale (float): the scale parameter of the distribution

        Returns:
            a float

        """
        fract = ((v_speed**exp_pwr_curve - v_in**exp_pwr_curve) /
                 (v_rate**exp_pwr_curve - v_in**exp_pwr_curve))

        return fract * _calc_weibull_probability(v_speed, k_shape, l_scale)

    # The rated power is expressed in units of MW but the harvested energy
    # equation calls for it in terms of Wh. Thus we multiply by a million to
    # get to Wh.
    rated_power = float(bio_parameters_dict['turbine_rated_pwr']) * 1000000

    # Get the rest of the inputs needed to compute harvested wind energy
    # from the dictionary so that it is in a more readable format
    exp_pwr_curve = int(bio_parameters_dict['exponent_power_curve'])
    air_density_standard = float(bio_parameters_dict['air_density'])
    v_rate = float(bio_parameters_dict['rated_wspd'])
    v_out = float(bio_parameters_dict['cut_out_wspd'])
    v_in = float(bio_parameters_dict['cut_in_wspd'])
    air_density_coef = float(bio_parameters_dict['air_density_coefficient'])
    losses = float(bio_parameters_dict['loss_parameter'])

    # Compute the mean air density, given by CKs formulas
    mean_air_density = air_density_standard - air_density_coef * hub_height

    # Fractional coefficient that lives outside the intregation for computing
    # the harvested wind energy
    fract_coef = rated_power * (mean_air_density / air_density_standard)

    # The coefficient that is multiplied by the integration portion of the
    # harvested wind energy equation
    scalar = _NUM_DAYS * 24 * fract_coef

    # The field names for the two outputs, Harvested Wind Energy and Wind
    # Density, to be added to the point shapefile
    density_field_name = 'Dens_W/m2'
    harvested_field_name = 'Harv_MWhr'

    def _compute_density_harvested_fields(wind_point_vector_path):
        """Compute the density and harvested energy.

        This is to help not open and pass around datasets / datasources.

        Parameters:
            wind_point_vector_path (str): path to a point shapefile to write
                the results to

        Returns:
            None.

        """
        # Open the wind points file to edit
        wind_points = gdal.OpenEx(wind_point_vector_path, 1)
        wind_points_layer = wind_points.GetLayer()

        # Get a feature so that we can get field indices that we will use
        # multiple times
        feature = wind_points_layer.GetFeature(0)

        # Get the indexes for the scale and shape parameters
        scale_index = feature.GetFieldIndex(_SCALE_KEY)
        shape_index = feature.GetFieldIndex(_SHAPE_KEY)
        LOGGER.debug('Scale/shape index : %s:%s', scale_index, shape_index)

        wind_points_layer.ResetReading()

        LOGGER.debug('Creating Harvest and Density Fields')
        # Create new fields for the density and harvested values
        for new_field_name in [density_field_name, harvested_field_name]:
            new_field = ogr.FieldDefn(new_field_name, ogr.OFTReal)
            wind_points_layer.CreateField(new_field)

        LOGGER.debug(
            'Entering Density and Harvest Calculations for each point')
        # For all the locations compute the Weibull density and
        # harvested wind energy. Save in a field of the feature
        for feat in wind_points_layer:
            # Get the scale and shape values
            scale_value = feat.GetField(scale_index)
            shape_value = feat.GetField(shape_index)

            # Integrate over the probability density function. 0 and 50 are
            # hard coded values set in CKs documentation
            density_results = integrate.quad(_calc_density_wind_energy, 0, 50,
                                             (shape_value, scale_value))

            # Compute the final wind power density value
            density_results = 0.5 * mean_air_density * density_results[0]

            # Integrate over the harvested wind energy function
            harv_results = integrate.quad(_calc_harvested_wind_energy, v_in,
                                          v_rate, (shape_value, scale_value))

            # Integrate over the Weibull probability function
            weibull_results = integrate.quad(_calc_weibull_probability, v_rate,
                                             v_out, (shape_value, scale_value))

            # Compute the final harvested wind energy value
            harvested_wind_energy = (
                scalar * (harv_results[0] + weibull_results[0]))

            # Convert harvested energy from Whr/yr to MWhr/yr by dividing by
            # 1,000,000
            harvested_wind_energy = harvested_wind_energy / 1000000.00

            # Now factor in the percent losses due to turbine
            # downtime (mechanical failure, storm damage, etc.)
            # and due to electrical resistance in the cables
            harvested_wind_energy = (1 - losses) * harvested_wind_energy

            # Finally, multiply the harvested wind energy by the number of
            # turbines to get the amount of energy generated for the entire farm
            harvested_wind_energy = harvested_wind_energy * number_of_turbines

            # Save the results to their respective fields
            for field_name, result_value in [(density_field_name,
                                              density_results),
                                             (harvested_field_name,
                                              harvested_wind_energy)]:
                out_index = feat.GetFieldIndex(field_name)
                feat.SetField(out_index, result_value)

            # Save the feature and set to None to clean up
            wind_points_layer.SetFeature(feat)

        wind_points = None

    # Compute Wind Density and Harvested Wind Energy, adding the values to the
    # points in the wind point shapefile
    _compute_density_harvested_fields(final_wind_point_vector_path)

    # Set paths for creating density and harvested rasters
    temp_density_raster_path = os.path.join(inter_dir,
                                            'temp_density%s.tif' % suffix)
    temp_harvested_raster_path = os.path.join(inter_dir,
                                              'temp_harvested%s.tif' % suffix)

    # Create rasters for density and harvested values
    LOGGER.info('Create Density Raster')
    pygeoprocessing.create_raster_from_vector_extents(
        final_wind_point_vector_path, temp_density_raster_path, pixel_size,
        _TARGET_DATA_TYPE, _TARGET_NODATA)

    LOGGER.info('Create Harvested Raster')
    pygeoprocessing.create_raster_from_vector_extents(
        final_wind_point_vector_path, temp_harvested_raster_path, pixel_size,
        _TARGET_DATA_TYPE, _TARGET_NODATA)

    # Interpolate points onto raster for density values and harvested values:
    LOGGER.info('Calculate Density Points')
    pygeoprocessing.interpolate_points(
        final_wind_point_vector_path,
        density_field_name, (temp_density_raster_path, 1),
        interpolation_mode='linear')

    LOGGER.info('Calculate Harvested Points')
    pygeoprocessing.interpolate_points(
        final_wind_point_vector_path,
        harvested_field_name, (temp_harvested_raster_path, 1),
        interpolation_mode='linear')

    def _mask_out_depth_dist(*rasters):
        """Return the value of an item in the list based on some condition.

        Return the value of an item in the list if and only if all other values
        are not a nodata value.

        Parameters:
            *rasters (list): a list of values as follows:
                rasters[0] - the density value (required)
                rasters[1] - the depth mask value (required)
                rasters[2] - the distance mask value (optional)

        Returns:
            out_array (np.array): an array of either _TARGET_NODATA or density
                values from rasters[0]

        """
        out_array = np.full(rasters[0].shape, _TARGET_NODATA, dtype=np.float32)
        nodata_mask = np.full(rasters[0].shape, False, dtype=bool)
        for array in rasters:
            nodata_mask = nodata_mask | (array == _TARGET_NODATA)
        out_array[~nodata_mask] = rasters[0][~nodata_mask]
        return out_array

    # Output paths for final Density and Harvested rasters after they've been
    # masked by depth and distance
    density_masked_path = os.path.join(
        out_dir, 'density_W_per_m2%s.tif' % suffix)
    harvested_masked_path = os.path.join(
        out_dir, 'harvested_energy_MWhr_per_yr%s.tif' % suffix)

    # List of paths to pass to raster_calculator for operations
    density_mask_list = [temp_density_raster_path, depth_mask_path]
    harvested_mask_list = [temp_harvested_raster_path, depth_mask_path]

    # If a distance mask was created then add it to the raster list to pass in
    # for masking out the output datasets
    try:
        density_mask_list.append(dist_mask_path)
        harvested_mask_list.append(dist_mask_path)
    except NameError:
        LOGGER.debug('NO Distance Mask to add to list')

    # Align and resize the mask rasters
    LOGGER.info('Align and resize the Density rasters')
    aligned_density_mask_list = [
        path.replace('%s.tif' % suffix, '_aligned%s.tif' % suffix)
        for path in density_mask_list
    ]

    aligned_harvested_mask_list = [
        path.replace('%s.tif' % suffix, '_aligned%s.tif' % suffix)
        for path in harvested_mask_list
    ]

    # Merge the density and harvest lists, and remove duplicates
    merged_mask_list = density_mask_list + [
        mask for mask in harvested_mask_list if mask not in density_mask_list
    ]
    merged_aligned_mask_list = aligned_density_mask_list + [
        mask for mask in aligned_harvested_mask_list
        if mask not in aligned_density_mask_list
    ]
    # Align and resize rasters in the density and harvest lists
    pygeoprocessing.align_and_resize_raster_stack(
        merged_mask_list, merged_aligned_mask_list,
        ['near'] * len(merged_mask_list), pixel_size, 'intersection')

    # Mask out any areas where distance or depth has determined that wind farms
    # cannot be located
    LOGGER.info('Mask out depth and [distance] areas from Density raster')
    pygeoprocessing.raster_calculator(
        [(path, 1) for path in aligned_density_mask_list], _mask_out_depth_dist,
        density_masked_path, _TARGET_DATA_TYPE, _TARGET_NODATA)

    LOGGER.info('Mask out depth and [distance] areas from Harvested raster')
    pygeoprocessing.raster_calculator(
        [(path, 1) for path in aligned_harvested_mask_list],
        _mask_out_depth_dist, harvested_masked_path, _TARGET_DATA_TYPE,
        _TARGET_NODATA)

    LOGGER.info('Wind Energy Biophysical Model completed')

    if 'valuation_container' in args and args['valuation_container'] is True:
        LOGGER.info('Starting Wind Energy Valuation Model')

        # path for final distance transform used in valuation calculations
        final_dist_raster_path = os.path.join(
            inter_dir, 'val_distance_trans%s.tif' % suffix)
    else:
        LOGGER.info('Valuation Not Selected. Model completed')
        return

    if 'grid_points_path' in args:
        # Handle Grid Points
        LOGGER.info('Grid Points Provided. Reading in the grid points')

        # Read the grid points csv, and convert it to land and grid dictionary
        grid_land_df = pandas.read_csv(args['grid_points_path'])
        # Convert column fields to upper cased to conform to the user's guide
        grid_land_df.columns = [
            field.upper() for field in grid_land_df.columns
        ]

        # Make separate dataframes based on 'TYPE'
        grid_df = grid_land_df.loc[(
            grid_land_df['TYPE'].str.upper() == 'GRID')]
        land_df = grid_land_df.loc[(
            grid_land_df['TYPE'].str.upper() == 'LAND')]

        # Convert the dataframes to dictionaries, using 'ID' (the index) as key
        grid_df.set_index('ID', inplace=True)
        grid_dict = grid_df.to_dict('index')
        land_df.set_index('ID', inplace=True)
        land_dict = land_df.to_dict('index')

        grid_vector_path = os.path.join(inter_dir,
                                        'val_grid_points%s.shp' % suffix)

        # Create a point shapefile from the grid point dictionary.
        # This makes it easier for future distance calculations and provides a
        # nice intermediate output for users
        _dictionary_to_point_vector(grid_dict, 'grid_points', grid_vector_path)

        # In case any of the above points lie outside the AOI, clip the
        # shapefiles and then project them to the AOI as well.
        grid_projected_vector_path = os.path.join(
            inter_dir, 'grid_point_projected_clipped%s.shp' % suffix)
        _clip_and_reproject_vector(grid_vector_path, aoi_vector_path,
                                   grid_projected_vector_path, inter_dir)

        # It is possible that NO grid points lie within the AOI, so we need to
        # handle both cases
        grid_vector = gdal.OpenEx(grid_projected_vector_path)
        grid_layer = grid_vector.GetLayer()
        if grid_layer.GetFeatureCount() != 0:
            LOGGER.debug('There are %s grid point(s) within AOI.' %
                         grid_layer.GetFeatureCount())
            # It's possible that no land points were provided, and we need to
            # handle both cases
            if land_dict:
                land_point_vector_path = os.path.join(
                    inter_dir, 'val_land_points%s.shp' % suffix)
                # Create a point shapefile from the land point dictionary.
                # This makes it easier for future distance calculations and
                # provides a nice intermediate output for users
                _dictionary_to_point_vector(land_dict, 'land_points',
                                            land_point_vector_path)

                # In case any of the above points lie outside the AOI, clip the
                # shapefiles and then project them to the AOI as well.
                land_projected_vector_path = os.path.join(
                    inter_dir, 'land_point_projected_clipped%s.shp' % suffix)
                _clip_and_reproject_vector(
                    land_point_vector_path, aoi_vector_path,
                    land_projected_vector_path, inter_dir)

                # It is possible that NO land point lie within the AOI, so we
                # need to handle both cases
                land_vector = gdal.OpenEx(land_projected_vector_path)
                land_layer = land_vector.GetLayer()
                if land_layer.GetFeatureCount() != 0:
                    LOGGER.debug('There are %d land point(s) within AOI.' %
                                 land_layer.GetFeatureCount())

                    # Calculate and add the shortest distances from each land
                    # point to the grid points and add them to the new field
                    LOGGER.info(
                        'Adding land to grid distances ("L2G") to land point '
                        'shapefile.')
                    _point_to_polygon_distance(land_projected_vector_path,
                                               grid_projected_vector_path,
                                               _LAND_TO_GRID_FIELD)

                    # Calculate distance raster
                    _calculate_distances_land_grid(
                        land_projected_vector_path, harvested_masked_path,
                        final_dist_raster_path, inter_dir)
                else:
                    LOGGER.debug(
                        'No land point lies within AOI. Energy transmission '
                        'cable distances are calculated from grid data.')
                    # Calculate distance raster
                    _calculate_distances_grid(grid_projected_vector_path,
                                              harvested_masked_path,
                                              final_dist_raster_path, inter_dir)
                land_layer = None
                land_vector = None

            else:
                LOGGER.info(
                    'No land points provided in the Grid Connection Points '
                    'CSV file. Energy transmission cable distances are '
                    'calculated from grid data.')

                # Calculate distance raster
                _calculate_distances_grid(grid_projected_vector_path,
                                          harvested_masked_path,
                                          final_dist_raster_path, inter_dir)
        else:
            LOGGER.debug(
                'No grid or land point lies in AOI. Energy transmission '
                'cable distances are not calculated.')
        grid_layer = None
        grid_vector = None

    else:
        LOGGER.info('Grid points not provided')
        LOGGER.debug(
            'No grid points, calculating distances using land polygon')
        # Since the grid points were not provided use the land polygon to get
        # near shore distances
        # The average land cable distance in km converted to meters
        avg_grid_distance = float(args['avg_grid_distance']) * 1000.0

        land_poly_dist_raster_path = os.path.join(
            inter_dir, 'land_poly_dist%s.tif' % suffix)

        _create_distance_raster(harvested_masked_path,
                                land_poly_proj_vector_path,
                                land_poly_dist_raster_path, inter_dir)

        def add_avg_dist_op(tmp_dist):
            """Convert distances to meters and add in avg_grid_distance

            Parameters:
                tmp_dist (np.array): an array of distances

            Returns:
                out_array (np.array): distance values in meters with average
                    grid to land distance factored in

            """
            out_array = np.full(
                tmp_dist.shape, _TARGET_NODATA, dtype=np.float32)
            valid_pixels_mask = (tmp_dist != _TARGET_NODATA)
            out_array[valid_pixels_mask] = tmp_dist[
                valid_pixels_mask] * mean_pixel_size + avg_grid_distance
            return out_array

        pygeoprocessing.raster_calculator(
            [(land_poly_dist_raster_path, 1)], add_avg_dist_op,
            final_dist_raster_path, _TARGET_DATA_TYPE, _TARGET_NODATA)

    # Get constants from val_parameters_dict to make it more readable
    # The length of infield cable in km
    infield_length = float(val_parameters_dict['infield_cable_length'])
    # The cost of infield cable in millions of dollars per km
    infield_cost = float(val_parameters_dict['infield_cable_cost'])
    # The cost of the foundation in millions of dollars
    foundation_cost = float(args['foundation_cost'])
    # The cost of each turbine unit in millions of dollars
    unit_cost = float(val_parameters_dict['turbine_cost'])
    # The installation cost as a decimal
    install_cost = float(val_parameters_dict['installation_cost'])
    # The miscellaneous costs as a decimal factor of capex_arr
    misc_capex_cost = float(val_parameters_dict['miscellaneous_capex_cost'])
    # The operations and maintenance costs as a decimal factor of capex_arr
    op_maint_cost = float(val_parameters_dict['operation_maintenance_cost'])
    # The discount rate as a decimal
    discount_rate = float(args['discount_rate'])
    # The cost to decommission the farm as a decimal factor of capex_arr
    decom = float(val_parameters_dict['decommission_cost'])
    # The mega watt value for the turbines in MW
    mega_watt = float(val_parameters_dict['turbine_rated_pwr'])
    # The distance at which AC switches over to DC power
    circuit_break = float(val_parameters_dict['ac_dc_distance_break'])
    # The coefficients for the AC/DC megawatt and cable cost from the CAP
    # function
    mw_coef_ac = float(val_parameters_dict['mw_coef_ac'])
    mw_coef_dc = float(val_parameters_dict['mw_coef_dc'])
    cable_coef_ac = float(val_parameters_dict['cable_coef_ac'])
    cable_coef_dc = float(val_parameters_dict['cable_coef_dc'])

    # The total mega watt capacity of the wind farm where mega watt is the
    # turbines rated power
    total_mega_watt = mega_watt * number_of_turbines

    # Total infield cable cost
    infield_cable_cost = infield_length * infield_cost * number_of_turbines
    LOGGER.debug('infield_cable_cost : %s', infield_cable_cost)

    # Total foundation cost
    total_foundation_cost = (foundation_cost + unit_cost) * number_of_turbines
    LOGGER.debug('total_foundation_cost : %s', total_foundation_cost)

    # Nominal Capital Cost (CAP) minus the cost of cable which needs distances
    cap_less_dist = infield_cable_cost + total_foundation_cost
    LOGGER.debug('cap_less_dist : %s', cap_less_dist)

    # Discount rate plus one to get that constant
    disc_const = discount_rate + 1.0
    LOGGER.debug('discount_rate : %s', disc_const)

    # Discount constant raised to the total time, a constant found in the NPV
    # calculation (1+i)^T
    disc_time = disc_const**time
    LOGGER.debug('disc_time : %s', disc_time)

    # The amount of CO2 not released into the atmosphere, with the
    # constant conversion factor provided in the users guide by
    # Rob Griffin
    carbon_coef = float(val_parameters_dict['carbon_coefficient'])

    def _calculate_carbon_op(harvested_arr):
        """Calculate the carbon offset from harvested array.

        Parameters:
            harvested_arr (np.array): an array of harvested energy values

        Returns:
            out_array (np.array): an array of carbon offset values

        """
        out_array = np.full(
            harvested_arr.shape, _TARGET_NODATA, dtype=np.float32)
        valid_pixels_mask = (harvested_arr != _TARGET_NODATA)

        # The energy value converted from MWhr/yr (Mega Watt hours as output
        # from CK's biophysical model equations) to kWhr for the
        # valuation model
        out_array[
            valid_pixels_mask] = harvested_arr[valid_pixels_mask] * \
            carbon_coef * 1000.0
        return out_array

    # paths for output rasters
    npv_raster_path = os.path.join(out_dir, 'npv_US_millions%s.tif' % suffix)
    levelized_raster_path = os.path.join(
        out_dir, 'levelized_cost_price_per_kWh%s.tif' % suffix)
    carbon_path = os.path.join(out_dir, 'carbon_emissions_tons%s.tif' % suffix)

    # create NPV and levelized cost rasters
    pygeoprocessing.new_raster_from_base(
        harvested_masked_path, npv_raster_path, _TARGET_DATA_TYPE,
        [_TARGET_NODATA])
    pygeoprocessing.new_raster_from_base(
        harvested_masked_path, levelized_raster_path, _TARGET_DATA_TYPE,
        [_TARGET_NODATA])

    # Open raster bands for writing
    npv_raster = gdal.OpenEx(npv_raster_path, gdal.OF_RASTER | gdal.GA_Update)
    npv_band = npv_raster.GetRasterBand(1)
    levelized_raster = gdal.OpenEx(
        levelized_raster_path, gdal.OF_RASTER | gdal.GA_Update)
    levelized_band = levelized_raster.GetRasterBand(1)

    for (harvest_block_info,
         harvest_block_data), (_, dist_block_data) in zip(
             pygeoprocessing.iterblocks((harvested_masked_path, 1)),
             pygeoprocessing.iterblocks((final_dist_raster_path, 1))):

        target_arr_shape = harvest_block_data.shape
        target_nodata_mask = (harvest_block_data == _TARGET_NODATA)

        # Total cable distance converted to kilometers
        cable_dist_arr = dist_block_data / 1000.0

        # The energy value converted from MWhr/yr (Mega Watt hours as output
        # from CK's biophysical model equations) to kWhr/yr for the
        # valuation model
        energy_val_arr = harvest_block_data * 1000.0

        # Calculate cable cost. The break at 'circuit_break' indicates the
        # difference in using AC and DC current systems
        circuit_mask = (cable_dist_arr <= circuit_break)
        cable_cost_arr = np.full(
            target_arr_shape, 0.0, dtype=np.float32)
        # Calculate AC cable cost
        cable_cost_arr[circuit_mask] = cable_dist_arr[
            circuit_mask] * cable_coef_ac + (mw_coef_ac * total_mega_watt)
        # Calculate DC cable cost
        cable_cost_arr[~circuit_mask] = cable_dist_arr[
            ~circuit_mask] * cable_coef_dc + (mw_coef_dc * total_mega_watt)
        # Mask out nodata values
        cable_cost_arr[target_nodata_mask] = _TARGET_NODATA

        # Compute the total CAP
        cap_arr = cap_less_dist + cable_cost_arr

        # Nominal total capital costs including installation and
        # miscellaneous costs (capex_arr)
        capex_arr = cap_arr / (1.0 - install_cost - misc_capex_cost)

        # The ongoing cost of the farm
        ongoing_capex_arr = op_maint_cost * capex_arr

        # The cost to decommission the farm
        decommish_capex_arr = decom * capex_arr / disc_time

        # Initialize the summation of the revenue less the ongoing costs,
        # adjusted for discount rate
        npv_arr = np.full(
            target_arr_shape, 0.0, dtype=np.float32)

        # Initialize the numerator summation part of the levelized cost
        levelized_num_arr = np.full(
            target_arr_shape, 0.0, dtype=np.float32)

        # Initialize and calculate the denominator summation value for
        # levelized cost of energy at year 0
        levelized_denom_arr = np.full(
            target_arr_shape, 0.0, dtype=np.float32)
        levelized_denom_arr = energy_val_arr / disc_const**0
        # Calculate the total NPV and the levelized cost over the lifespan of
        # the wind farm. Starting at year 1, because year 0 yields no revenue
        for year in xrange(1, len(price_list)):
            # Dollar per kiloWatt hour of that year
            dollar_per_kwh = float(price_list[year])

            # The price per kWh for energy converted to units of millions of
            # dollars to correspond to the units for valuation costs
            mill_dollar_per_kwh = dollar_per_kwh / 1000000.0

            # The revenue in millions of dollars for the wind farm. The
            # energy_val_arr is in kWh/yr
            rev_arr = energy_val_arr * mill_dollar_per_kwh

            # Calculate the net present value (NPV), the summation of the net
            # revenue from power generation, adjusted for discount rate
            npv_arr = (
                npv_arr + (rev_arr - ongoing_capex_arr) / disc_const**year)

            # Calculate the cumulative numerator summation value
            levelized_num_arr = levelized_num_arr + (
                (ongoing_capex_arr / disc_const**year))

            # Calculate the cumulative denominator summation value
            levelized_denom_arr = levelized_denom_arr + (
                energy_val_arr / disc_const**year)

        # Calculate the final NPV by subtracting other costs from the NPV
        npv_arr[target_nodata_mask] = _TARGET_NODATA
        npv_arr[~target_nodata_mask] = npv_arr[~target_nodata_mask] - \
            decommish_capex_arr[~target_nodata_mask] - \
            capex_arr[~target_nodata_mask]

        # Calculate the levelized cost of energy, converting from millions of
        # dollars to dollars
        levelized_arr = (
            (levelized_num_arr + decommish_capex_arr + capex_arr) /
            levelized_denom_arr) * 1000000.0
        levelized_arr[target_nodata_mask] = _TARGET_NODATA

        npv_band.WriteArray(npv_arr,
                            xoff=harvest_block_info['xoff'],
                            yoff=harvest_block_info['yoff'])
        npv_band.FlushCache()

        levelized_band.WriteArray(levelized_arr,
                                  xoff=harvest_block_info['xoff'],
                                  yoff=harvest_block_info['yoff'])
        levelized_band.FlushCache()

    npv_band = None
    npv_raster.FlushCache()
    npv_raster = None

    levelized_band = None
    levelized_raster.FlushCache()
    levelized_raster = None

    pygeoprocessing.raster_calculator([(harvested_masked_path, 1)],
                                      _calculate_carbon_op, carbon_path,
                                      _TARGET_DATA_TYPE, _TARGET_NODATA)
    LOGGER.info('Wind Energy Valuation Model Completed')


def _point_to_polygon_distance(base_point_vector_path, base_polygon_vector_path,
                               dist_field_name):
    """Calculate the distances from points to the nearest polygon.

    Distances are calculated from points in a point geometry shapefile to the
    nearest polygon from a polygon shapefile. Both shapefiles must be
    projected in meters

    Parameters:
        base_point_vector_path (str): a path to an OGR point geometry
            shapefile projected in meters
        base_polygon_vector_path (str): a path to an OGR polygon shapefile
            projected in meters
        dist_field_name (str): the name of the new distance field to be
            added to the attribute table of base_point_vector

    Returns:
        None.

    """
    LOGGER.info('Starting _point_to_polygon_distance.')
    point_vector = gdal.OpenEx(
        base_point_vector_path, gdal.OF_VECTOR | gdal.GA_Update)
    poly_vector = gdal.OpenEx(
        base_polygon_vector_path, gdal.OF_VECTOR | gdal.GA_ReadOnly)

    poly_layer = poly_vector.GetLayer()
    # List to store the polygons geometries as shapely objects
    poly_list = []

    LOGGER.info('Loading the polygons into Shapely')
    for poly_feat in poly_layer:
        # Get the geometry of the polygon in WKT format
        poly_wkt = poly_feat.GetGeometryRef().ExportToWkt()
        # Load the geometry into shapely making it a shapely object
        shapely_polygon = shapely.wkt.loads(poly_wkt)
        # Add the shapely polygon geometry to a list, but first simplify the
        # geometry which smooths the edges making operations a lot faster
        poly_list.append(
            shapely_polygon.simplify(0.01, preserve_topology=False))

    # Take the union over the list of polygons to get one defined polygon object
    LOGGER.info('Get the collection of polygon geometries by taking the union')
    polygon_collection = shapely.ops.unary_union(poly_list)

    point_layer = point_vector.GetLayer()
    # Create a new distance field based on the name given
    dist_field_defn = ogr.FieldDefn(dist_field_name, ogr.OFTReal)
    point_layer.CreateField(dist_field_defn)

    LOGGER.info('Loading the points into shapely')
    for point_feat in point_layer:
        # Get the geometry of the point in WKT format
        point_wkt = point_feat.GetGeometryRef().ExportToWkt()
        # Load the geometry into shapely making it a shapely object
        shapely_point = shapely.wkt.loads(point_wkt)
        # Get the distance in meters and convert to km
        point_dist = shapely_point.distance(polygon_collection) / 1000.0
        # Add the distance value to the new field and set to the feature
        point_feat.SetField(dist_field_name, point_dist)
        point_layer.SetFeature(point_feat)

    point_layer = None
    point_vector = None
    poly_layer = None
    poly_vector = None

    LOGGER.info('Finished _point_to_polygon_distance.')


def _read_csv_wind_parameters(csv_path, parameter_list):
    """Construct a dictionary from a csv file given a list of keys.

    The list of keys corresponds to the parameters names in 'csv_path' which
    are represented in the first column of the file.

    Parameters:
        csv_path (str): a path to a CSV file where every row is a parameter
            with the parameter name in the first column followed by the value
            in the second column
        parameter_list (list) : a List of strs that represent the parameter
            names to be found in 'csv_path'. These strs will be the keys in
            the returned dictionary

    Returns: a Dictionary where the 'parameter_list' strs are the
            keys that have values pulled from 'csv_path'

    """
    # use the parameters in the first column as indeces for the dataframe
    wind_param_df = pandas.read_csv(csv_path, header=None, index_col=0)
    wind_param_df.index = wind_param_df.index.str.lower()
    # only get the required parameters and leave out the rest
    wind_param_df = wind_param_df[wind_param_df.index.isin(parameter_list)]
    wind_dict = wind_param_df.to_dict()[1]

    return wind_dict


def _mask_by_distance(base_raster_path, min_dist, max_dist, out_nodata,
                      target_raster_path):
    """Create a raster whose pixel values are bound by min and max distances.

    Parameters:
        base_raster_path (str): path to a raster with distance values.
        min_dist (int): the minimum distance allowed in meters.
        max_dist (int): the maximum distance allowed in meters.
        target_raster_path (str): path output to the raster masked by
            distance values.
        out_nodata (float): the nodata value of the raster.

    Returns:
        None.

    """
    mean_pixel_size, _ = utils.mean_pixel_size_and_area(
        pygeoprocessing.get_raster_info(base_raster_path)['pixel_size'])
    raster_nodata = pygeoprocessing.get_raster_info(base_raster_path)[
        'nodata'][0]

    def _dist_mask_op(dist_arr):
        """Mask & multiply distance values by min/max values & cell size."""
        out_array = np.full(dist_arr.shape, out_nodata, dtype=np.float32)
        valid_pixels_mask = ((dist_arr != raster_nodata) &
                             (dist_arr >= min_dist) & (dist_arr <= max_dist))
        out_array[
            valid_pixels_mask] = dist_arr[valid_pixels_mask] * mean_pixel_size
        return out_array

    pygeoprocessing.raster_calculator([(base_raster_path, 1)], _dist_mask_op,
                                      target_raster_path, _TARGET_DATA_TYPE,
                                      out_nodata)


def _create_distance_raster(base_raster_path, base_vector_path,
                            target_dist_raster_path, work_dir):
    """Create and rasterize vector onto a raster, and calculate dist transform.

    Create a raster where the pixel values represent the euclidean distance to
    the vector.

    Parameters:
        base_raster_path (str): path to raster to create a new raster from.
        base_vector_path (str): path to vector to be rasterized.
        target_dist_raster_path (str): path to raster with distance transform.
        work_dir (str): path to create a temp folder for saving files.

    Returns:
        None

    """
    LOGGER.info("Starting _create_distance_raster")
    temp_dir = tempfile.mkdtemp(dir=work_dir, prefix='dist-raster-')

    rasterized_raster_path = os.path.join(temp_dir, 'rasterized_raster.tif')

    # Create a new raster based on the given base raster and fill with 0's
    # to set up for distance transform
    pygeoprocessing.new_raster_from_base(
        base_raster_path,
        rasterized_raster_path,
        gdal.GDT_Byte,
        band_nodata_list=[255],
        fill_value_list=[0])

    # Burn vector onto the raster to set up for distance transform
    pygeoprocessing.rasterize(
        base_vector_path,
        rasterized_raster_path,
        burn_values=[1],
        option_list=["ALL_TOUCHED=TRUE"])

    # Calculate euclidean distance transform
    pygeoprocessing.distance_transform_edt((rasterized_raster_path, 1),
                                           target_dist_raster_path)

    # Set the nodata value of output raster to _TARGET_NODATA
    target_dist_raster = gdal.OpenEx(
        target_dist_raster_path, gdal.OF_RASTER | gdal.GA_Update)
    for band in range(1, target_dist_raster.RasterCount+1):
        target_band = target_dist_raster.GetRasterBand(band)
        target_band.SetNoDataValue(_TARGET_NODATA)
        target_band.FlushCache()
        target_band = None
    target_dist_raster.FlushCache()
    target_dist_raster = None

    shutil.rmtree(temp_dir, ignore_errors=True)
    LOGGER.info("Finished _create_distance_raster")


def _read_csv_wind_data(wind_data_path, hub_height):
    """Unpack the csv wind data into a dictionary.

    Parameters:
        wind_data_path (str): a path for the csv wind data file with header
            of: "LONG","LATI","LAM","K","REF"
        hub_height (int): the hub height to use for calculating Weibull
            parameters and wind energy values

    Returns:
        A dictionary where the keys are lat/long tuples which point
            to dictionaries that hold wind data at that location.

    """
    wind_point_df = pandas.read_csv(wind_data_path)

    # Calculate scale value at new hub height given reference values.
    # See equation 3 in users guide
    wind_point_df.rename(columns={'LAM': 'REF_LAM'}, inplace=True)
    wind_point_df['LAM'] = wind_point_df.apply(
        lambda row: row.REF_LAM * (hub_height / row.REF)**_ALPHA, axis=1)
    wind_point_df.drop(['REF'], axis=1)  # REF is not needed after calculation
    wind_dict = wind_point_df.to_dict('index')  # so keys will be 0, 1, 2, ...

    return wind_dict


def _dictionary_to_point_vector(base_dict_data, layer_name, target_vector_path):
    """Create a point shapefile from a dictionary.

    The point shapefile created is not projected and uses latitude and
        longitude for its geometry.

    Parameters:
        base_dict_data (dict): a python dictionary with keys being unique id's
            that point to sub-dictionaries that have key-value pairs. These
            inner key-value pairs will represent the field-value pair for the
            point features. At least two fields are required in the sub-
            dictionaries. All the keys in the sub dictionary should have the
            same name and order. All the values in the sub dictionary should
            have the same type 'LATI' and 'LONG'. These fields determine the
            geometry of the point.
            0 : {'TYPE':GRID, 'LATI':41, 'LONG':-73, ...},
            1 : {'TYPE':GRID, 'LATI':42, 'LONG':-72, ...},
            2 : {'TYPE':GRID, 'LATI':43, 'LONG':-72, ...},
        layer_name (str): a python str for the name of the layer
        target_vector_path (str): a path to the output path of the point
            vector.

    Returns:
        None

    """
    # If the target_vector_path exists delete it
    output_driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(target_vector_path):
        output_driver.DeleteDataSource(target_vector_path)

    target_vector = output_driver.CreateDataSource(target_vector_path)

    # Set the spatial reference to WGS84 (lat/long)
    source_sr = osr.SpatialReference()
    source_sr.SetWellKnownGeogCS("WGS84")

    output_layer = target_vector.CreateLayer(layer_name, source_sr,
                                             ogr.wkbPoint)

    # Outer unique keys
    outer_keys = base_dict_data.keys()

    # Construct a list of fields to add from the keys of the inner dictionary
    field_list = base_dict_data[outer_keys[0]].keys()

    # Create a dictionary to store what variable types the fields are
    type_dict = {}
    for field in field_list:
        field_type = None
        # Get a value from the field
        val = base_dict_data[outer_keys[0]][field]
        # Check to see if the value is a str of characters or a number. This
        # will determine the type of field created in the shapefile
        if isinstance(val, str):
            type_dict[field] = 'str'
            field_type = ogr.OFTString
        else:
            type_dict[field] = 'number'
            field_type = ogr.OFTReal
        output_field = ogr.FieldDefn(field, field_type)
        output_layer.CreateField(output_field)

    # For each inner dictionary (for each point) create a point and set its
    # fields
    for point_dict in base_dict_data.itervalues():
        latitude = float(point_dict['LATI'])
        longitude = float(point_dict['LONG'])

        geom = ogr.Geometry(ogr.wkbPoint)
        geom.AddPoint_2D(longitude, latitude)

        output_feature = ogr.Feature(output_layer.GetLayerDefn())

        for field_name in point_dict:
            field_index = output_feature.GetFieldIndex(field_name)
            output_feature.SetField(field_index, point_dict[field_name])

        output_feature.SetGeometryDirectly(geom)
        output_layer.CreateFeature(output_feature)
        output_feature = None

    output_layer.SyncToDisk()


def _clip_to_projection_with_square_pixels(base_raster_path, clip_vector_path,
                                           target_raster_path):
    """Clip raster with vector into projected coordinate system.

    If base raster is not already projected, choose a suitable UTM zone. If
    pixel size of target raster is not square, the minimum absolute value will
    be used for target_pixel_size.

    Parameters:
        base_raster_path (str): path to base raster.
        clip_vector_path (str): path to base clip vector.
        target_raster_path (str): path to output clipped raster with square
            pixel size.

    Returns:
        None.

    """
    base_raster_info = pygeoprocessing.get_raster_info(base_raster_path)
    clip_vector_info = pygeoprocessing.get_vector_info(clip_vector_path)

    base_raster_srs = osr.SpatialReference()
    base_raster_srs.ImportFromWkt(base_raster_info['projection'])

    if not base_raster_srs.IsProjected():
        wgs84_sr = osr.SpatialReference()
        wgs84_sr.ImportFromEPSG(4326)
        clip_wgs84_bounding_box = pygeoprocessing.transform_bounding_box(
            clip_vector_info['bounding_box'], clip_vector_info['projection'],
            wgs84_sr.ExportToWkt())

        base_raster_bounding_box = pygeoprocessing.transform_bounding_box(
            base_raster_info['bounding_box'], base_raster_info['projection'],
            wgs84_sr.ExportToWkt())

        target_bounding_box_wgs84 = pygeoprocessing.merge_bounding_box_list(
            [clip_wgs84_bounding_box, base_raster_bounding_box], 'intersection')

        clip_vector_srs = osr.SpatialReference()
        clip_vector_srs.ImportFromWkt(clip_vector_info['projection'])

        centroid_x = (
            target_bounding_box_wgs84[2] + target_bounding_box_wgs84[0]) / 2
        centroid_y = (
            target_bounding_box_wgs84[3] + target_bounding_box_wgs84[1]) / 2
        utm_code = (math.floor((centroid_x + 180) / 6) % 60) + 1
        utm_code = (math.floor((centroid_x + 180.0) / 6) % 60) + 1
        lat_code = 6 if centroid_y > 0 else 7
        epsg_code = int('32%d%02d' % (lat_code, utm_code))
        target_srs = osr.SpatialReference()
        target_srs.ImportFromEPSG(epsg_code)
        target_bounding_box = pygeoprocessing.transform_bounding_box(
            target_bounding_box_wgs84, wgs84_sr.ExportToWkt(),
            target_srs.ExportToWkt())

        target_pixel_size = _convert_degree_pixel_size_to_square_meters(
            base_raster_info['pixel_size'], centroid_y)

        pygeoprocessing.warp_raster(
            base_raster_path,
            target_pixel_size,
            target_raster_path,
            None,
            target_bb=target_bounding_box,
            target_sr_wkt=target_srs.ExportToWkt(),
            vector_mask_options={'mask_vector_path': clip_vector_path})
    else:
        pygeoprocessing.align_and_resize_raster_stack(
            [base_raster_path], [target_raster_path], ['near'],
            base_raster_info['pixel_size'],
            'intersection',
            base_vector_path_list=[clip_vector_path],
            target_sr_wkt=base_raster_info['projection'],
            vector_mask_options={'mask_vector_path': clip_vector_path})


def _convert_degree_pixel_size_to_square_meters(pixel_size, center_lat):
    """Calculate meter size of a wgs84 square pixel.

    Adapted from: https://gis.stackexchange.com/a/127327/2397. If the pixel
    is not square, this function will use the minimum absolute value from the
    pixel dimension in the output meter_pixel_size_tuple.

    Parameters:
        pixel_size (tuple): [xsize, ysize] in degrees (float).
        center_lat (float): latitude of the center of the pixel. Note this
            value +/- half the `pixel-size` must not exceed 90/-90 degrees
            latitude or an invalid area will be calculated.

    Returns:
        `meter_pixel_size_tuple` with minimum absolute value in the pixel sizes

    """
    m1 = 111132.92
    m2 = -559.82
    m3 = 1.175
    m4 = -0.0023
    p1 = 111412.84
    p2 = -93.5
    p3 = 0.118

    lat = center_lat * math.pi / 180
    latlen = (m1 + m2 * math.cos(2 * lat) + m3 * math.cos(4 * lat) +
              m4 * math.cos(6 * lat))
    longlen = abs(p1 * math.cos(lat) + p2 * math.cos(3 * lat) +
                  p3 * math.cos(5 * lat))
    x_meter_size = longlen * pixel_size[0]
    y_meter_size = latlen * pixel_size[1]
    meter_pixel_size_tuple = (x_meter_size, y_meter_size)
    if not np.isclose(x_meter_size, y_meter_size):
        min_meter_size = np.min(np.absolute(meter_pixel_size_tuple))
        meter_pixel_size_tuple = (min_meter_size, -min_meter_size)

    return meter_pixel_size_tuple


def _wind_data_to_point_vector(dict_data,
                               layer_name,
                               target_vector_path,
                               ref_projection_wkt=None):
    """Create a point shapefile given a dictionary of the wind data fields.

    Parameters:
        dict_data (dict): a dictionary with the wind data, where the keys
            are tuples of the lat/long coordinates:
            {
            1 : {'LATI':97, 'LONG':43, 'LAM':6.3, 'K':2.7, 'REF':10},
            2 : {'LATI':55, 'LONG':51, 'LAM':6.2, 'K':2.4, 'REF':10},
            3 : {'LATI':73, 'LONG':47, 'LAM':6.5, 'K':2.3, 'REF':10}
            }
        layer_name (str): the name of the layer.
        target_vector_path (str): path to the output destination of the
            shapefile.
        ref_projection_wkt (str): reference projection of in Well Known Text.

    Returns:
        None

    """
    LOGGER.info('Entering _wind_data_to_point_vector')

    # If the target_vector_path exists delete it
    if os.path.isfile(target_vector_path):
        driver = ogr.GetDriverByName('ESRI Shapefile')
        driver.DeleteDataSource(target_vector_path)

    target_driver = ogr.GetDriverByName('ESRI Shapefile')
    target_vector = target_driver.CreateDataSource(target_vector_path)
    target_sr = osr.SpatialReference()
    target_sr.SetWellKnownGeogCS("WGS84")

    if ref_projection_wkt:
        ref_sr = osr.SpatialReference(wkt=ref_projection_wkt)
        if ref_sr.IsProjected:
            # Get coordinate transformation between two projections
            coord_trans = osr.CoordinateTransformation(
                target_sr, ref_sr)
            need_geotranform = True
        else:
            need_geotranform = False
    else:
        need_geotranform = False

    if need_geotranform:
        target_layer = target_vector.CreateLayer(
            layer_name, ref_sr, ogr.wkbPoint)
    else:
        target_layer = target_vector.CreateLayer(
            layer_name, target_sr, ogr.wkbPoint)

    # Construct a list of fields to add from the keys of the inner dictionary
    field_list = dict_data[dict_data.keys()[0]].keys()
    LOGGER.debug('field_list : %s', field_list)

    LOGGER.info('Creating fields for the target vector')
    for field in field_list:
        target_field = ogr.FieldDefn(field, ogr.OFTReal)
        target_layer.CreateField(target_field)

    LOGGER.info('Entering iteration to create and set the features')
    # For each inner dictionary (for each point) create a point
    for point_dict in dict_data.itervalues():
        geom = ogr.Geometry(ogr.wkbPoint)
        latitude = float(point_dict['LATI'])
        longitude = float(point_dict['LONG'])
        # When projecting to WGS84, extents -180 to 180 are used for
        # longitude. In case input longitude is from -360 to 0 convert
        if longitude < -180:
            longitude += 360
        if need_geotranform:
            point_x, point_y, point_z = coord_trans.TransformPoint(
                longitude, latitude)
            geom.AddPoint(point_x, point_y)
        else:
            geom.AddPoint_2D(longitude, latitude)

        target_feature = ogr.Feature(target_layer.GetLayerDefn())
        target_layer.CreateFeature(target_feature)

        for field_name in point_dict:
            field_index = target_feature.GetFieldIndex(field_name)
            target_feature.SetField(field_index, point_dict[field_name])

        target_feature.SetGeometryDirectly(geom)
        target_layer.SetFeature(target_feature)
        target_feature = None

    LOGGER.info('Finished _wind_data_to_point_vector')
    target_vector = None


def _clip_and_reproject_vector(base_vector_path, clip_vector_path,
                               target_vector_path, work_dir):
    """Clip a vector against an AOI and output result in AOI coordinates.

    Parameters:
        base_vector_path (str): path to a base vector
        clip_vector_path (str): path to an AOI vector
        target_vector_path (str): desired output path to write the
            clipped base against AOI in AOI's coordinate system.
        work_dir (str): path to create a temp folder for saving files.

    Returns:
        None.
    """
    LOGGER.info('Entering _clip_and_reproject_vector')
    temp_dir = tempfile.mkdtemp(dir=work_dir, prefix='clip-reproject-')

    # Get the base and target spatial reference in Well Known Text
    base_sr_wkt = pygeoprocessing.get_vector_info(base_vector_path)[
        'projection']
    target_sr_wkt = pygeoprocessing.get_vector_info(clip_vector_path)[
        'projection']

    # Create path for the reprojected shapefile
    clipped_vector_path = os.path.join(
        temp_dir, 'clipped_vector.shp')
    reprojected_clip_path = os.path.join(
        temp_dir, 'reprojected_clip_vector.shp')

    if base_sr_wkt != target_sr_wkt:
        # Reproject clip vector to the spatial reference of the base vector.
        # Note: reproject_vector can be expensive if vector has many features.
        pygeoprocessing.reproject_vector(
            clip_vector_path, base_sr_wkt, reprojected_clip_path)

    # Clip the shapefile to the AOI
    _clip_vector_by_vector(
        base_vector_path, reprojected_clip_path, clipped_vector_path)

    # Reproject the clipped base vector to the spatial reference of clip vector
    pygeoprocessing.reproject_vector(
        clipped_vector_path, target_sr_wkt, target_vector_path)

    shutil.rmtree(temp_dir, ignore_errors=True)
    LOGGER.info('Finished _clip_and_reproject_vector')


def _clip_vector_by_vector(
        base_vector_path, clip_vector_path, target_vector_path):
    """Create a new target vector where base features are contained in the
        polygon in clip_vector_path. Assumes all data are in the same
        projection.

    Parameters:
        base_vector_path (str): path to a vector to clip.
        clip_vector_path (str): path to a polygon vector for clipping.
        target_vector_path (str): output path for the clipped vector.

    Returns:
        None.

    """
    LOGGER.info('Entering _clip_vector_by_vector')

    # Get layer and geometry informations from path
    base_vector = gdal.OpenEx(base_vector_path)
    base_layer = base_vector.GetLayer()
    base_layer_defn = base_layer.GetLayerDefn()
    base_geom_type = base_layer.GetGeomType()

    clip_vector = gdal.OpenEx(clip_vector_path)
    clip_layer = clip_vector.GetLayer()

    # Create a target vector based on the properties of base vector
    target_driver = ogr.GetDriverByName('ESRI Shapefile')
    target_vector = target_driver.CreateDataSource(target_vector_path)
    target_layer = target_vector.CreateLayer(base_layer_defn.GetName(),
                                             base_layer.GetSpatialRef(),
                                             base_geom_type)
    base_layer.Clip(clip_layer, target_layer)

    target_layer = None
    target_vector = None
    clip_vector = None
    clip_vector = None
    base_layer = None
    base_vector = None
    LOGGER.info('Finished _clip_vector_by_vector')


def _calculate_distances_land_grid(base_point_vector_path, base_raster_path,
                                   target_dist_raster_path, work_dir):
    """Creates a distance transform raster.

    The distances are calculated based on the shortest distances of each point
    feature in 'base_point_vector_path' and each feature's 'L2G' field.

    Parameters:
        base_point_vector_path (str): path to an OGR shapefile that has
            the desired features to get the distance from.
        base_raster_path (str): path to a GDAL raster that is used to
            get the proper extents and configuration for the new raster.
        target_dist_raster_path (str): path to a GDAL raster for the final
            distance transform raster output.
        work_dir (str): path to create a temp folder for saving files.

    Returns:
        None.

    """
    LOGGER.info('Starting _calculate_distances_land_grid.')
    temp_dir = tempfile.mkdtemp(dir=work_dir, prefix='calc-dist-land')

    # Open the point shapefile and get the layer
    base_point_vector = gdal.OpenEx(base_point_vector_path)
    base_point_layer = base_point_vector.GetLayer()
    # A list to hold the land to grid distances in order for each point
    # features 'L2G' field
    l2g_dist = []
    # A list to hold the individual distance transform path's in order
    land_point_dist_raster_path_list = []

    # Get the mean pixel size to calculate minimum distance from land to grid
    mean_pixel_size, _ = utils.mean_pixel_size_and_area(
        pygeoprocessing.get_raster_info(base_raster_path)['pixel_size'])

    # Get the original layer definition which holds needed attribute values
    base_layer_defn = base_point_layer.GetLayerDefn()
    output_driver = ogr.GetDriverByName('ESRI Shapefile')
    single_feature_vector_path = os.path.join(temp_dir, 'single_feature.shp')
    target_vector = output_driver.CreateDataSource(single_feature_vector_path)

    # Create the new layer for target_vector using same name and
    # geometry type from base_vector as well as spatial reference
    target_layer = target_vector.CreateLayer(base_layer_defn.GetName(),
                                             base_point_layer.GetSpatialRef(),
                                             base_layer_defn.GetGeomType())

    # Get the number of fields in original_layer
    base_field_count = base_layer_defn.GetFieldCount()

    # For every field, create a duplicate field and add it to the new
    # shapefiles layer
    for fld_index in range(base_field_count):
        base_field = base_layer_defn.GetFieldDefn(fld_index)
        target_field = ogr.FieldDefn(base_field.GetName(),
                                     base_field.GetType())
        # NOT setting the WIDTH or PRECISION because that seems to be
        # unneeded and causes interesting OGR conflicts
        target_layer.CreateField(target_field)

    # Create a new shapefile with only one feature to burn onto a raster
    # in order to get the distance transform based on that one feature
    for feature_index, point_feature in enumerate(base_point_layer):
        # Get the point features land to grid value and add it to the list
        field_index = point_feature.GetFieldIndex('L2G')
        l2g_dist.append(float(point_feature.GetField(field_index)))

        # Copy original_datasource's feature and set as new shapes feature
        output_feature = ogr.Feature(feature_def=target_layer.GetLayerDefn())

        # Since the original feature is of interest add its fields and
        # Values to the new feature from the intersecting geometries
        # The False in SetFrom() signifies that the fields must match
        # exactly
        output_feature.SetFrom(point_feature, False)
        target_layer.CreateFeature(output_feature)
        target_vector.SyncToDisk()
        target_layer.DeleteFeature(point_feature.GetFID())

        dist_raster_path = os.path.join(temp_dir,
                                        'dist_%s.tif' % feature_index)
        _create_distance_raster(base_raster_path, single_feature_vector_path,
                                dist_raster_path, work_dir)
        # Add each features distance transform result to list
        land_point_dist_raster_path_list.append(dist_raster_path)

    target_layer = None
    target_vector = None
    base_point_layer = None
    base_point_vector = None
    l2g_dist_array = np.array(l2g_dist)

    def _min_land_ocean_dist(*grid_distances):
        """Aggregate each features distance transform output and create one
            distance output that has the shortest distances combined with each
            features land to grid distance

        Parameters:
            *grid_distances (numpy.ndarray): a variable number of numpy.ndarray

        Returns:
            a numpy.ndarray of the shortest distances

        """
        # Get the shape of the incoming numpy arrays
        # Initialize with land to grid distances from the first array
        min_distances = np.min(grid_distances, axis=0)
        min_land_grid_dist = l2g_dist_array[np.argmin(grid_distances, axis=0)]
        return min_distances * mean_pixel_size + min_land_grid_dist

    pygeoprocessing.raster_calculator(
        [(path, 1)
         for path in land_point_dist_raster_path_list], _min_land_ocean_dist,
        target_dist_raster_path, _TARGET_DATA_TYPE, _TARGET_NODATA)

    shutil.rmtree(temp_dir, ignore_errors=True)

    LOGGER.info('Finished _calculate_distances_land_grid.')


def _calculate_distances_grid(grid_vector_path, harvested_masked_path,
                              final_dist_raster_path, work_dir):
    """Creates a distance transform raster from an OGR shapefile.

    The function first burns the features from 'grid_vector_path' onto a raster
    using 'harvested_masked_path' as the base for that raster. It then does a
    distance transform from those locations and converts from pixel distances
    to distance in meters.

    Parameters:
        grid_vector_path (str) a path to an OGR shapefile that has the
            desired features to get the distance from
        harvested_masked_path (str): a path to a GDAL raster that is used to
            get the proper extents and configuration for new rasters
        final_dist_raster_path (str) a path to a GDAL raster for the final
            distance transform raster output
        work_dir (str): path to create a temp folder for saving files.

    Returns:
        None

    """
    LOGGER.info('Starting _calculate_distances_land_grid.')
    temp_dir = tempfile.mkdtemp(dir=work_dir, prefix='calc-dist-grid-')

    # Get nodata value to use in raster creation and masking
    out_nodata = pygeoprocessing.get_raster_info(harvested_masked_path)[
        'nodata'][0]
    # Get pixel size from biophysical output
    mean_pixel_size, _ = utils.mean_pixel_size_and_area(
        pygeoprocessing.get_raster_info(harvested_masked_path)['pixel_size'])

    grid_poly_dist_raster_path = os.path.join(temp_dir, 'grid_poly_dist.tif')

    _create_distance_raster(harvested_masked_path, grid_vector_path,
                            grid_poly_dist_raster_path, work_dir)

    def _dist_meters_op(tmp_dist):
        """Multiply the pixel value of a raster by the mean pixel size.

        Parameters:
            tmp_dist (np.array): an nd numpy array

        Returns:
            out_array (np.array): an array multiplied by a pixel size
        """
        out_array = np.full(tmp_dist.shape, out_nodata, dtype=np.float32)
        valid_pixels_mask = (tmp_dist != out_nodata)
        out_array[
            valid_pixels_mask] = tmp_dist[valid_pixels_mask] * mean_pixel_size
        return out_array

    pygeoprocessing.raster_calculator([(grid_poly_dist_raster_path, 1)],
                                      _dist_meters_op, final_dist_raster_path,
                                      _TARGET_DATA_TYPE, out_nodata)

    shutil.rmtree(temp_dir, ignore_errors=True)


@validation.invest_validator
def validate(args, limit_to=None):
    """Validate an input dictionary for Wind Energy.

    Parameters:
        args (dict): The args dictionary.

        limit_to=None (str or None): If a str key, only this args parameter
            will be validated.  If ``None``, all args parameters will be
            validated.

    Returns:
        A list of tuples where tuple[0] is an iterable of keys that the error
        message applies to and tuple[1] is the str validation warning.

    """
    warnings = []
    keys_missing_value = set([])
    missing_keys = set([])

    required_keys = [
        'workspace_dir',
        'wind_data_path',
        'bathymetry_path',
        'global_wind_parameters_path',
        'turbine_parameters_path',
        'number_of_turbines',
        'min_depth',
        'max_depth',
    ]

    # If we're doing valuation, min and max distance are required.
    if 'valuation_container' in args and args['valuation_container']:
        for key in ('min_distance', 'max_distance'):
            if args[key] in ('', None):
                warnings.append(([key], 'Value must be defined.'))

        required_keys.extend([
            'discount_rate',
            'foundation_cost',
        ])

        if limit_to in ('price_table', None):
            if 'price_table' in args and args['price_table'] not in (True,
                                                                     False):
                warnings.append((['price_table'],
                                 'Parameter must be either True or False'))
            if args['price_table']:
                required_keys.append('wind_schedule')
            else:
                required_keys.extend(['wind_price', 'rate_change'])

        missing_distance_key = 2
        try:
            if args['avg_grid_distance'] in ('', None):
                missing_distance_key -= 1
        except KeyError:
            missing_distance_key -= 1
            try:
                if args['grid_points_path'] in ('', None):
                    missing_distance_key -= 1
            except KeyError:
                missing_distance_key -= 1
        if missing_distance_key > 1:
            return [
                'Either avg_grid_distance or grid_points_path must be '
                'provided.'
            ]

    for required_key in required_keys:
        try:
            if args[required_key] in ('', None):
                keys_missing_value.add(required_key)
        except KeyError:
            missing_keys.add(required_key)

    if missing_keys:
        return [(missing_keys,
                 'Required keys are missing from args: %s' % ', '.join(
                     sorted(missing_keys)))]

    if keys_missing_value:
        warnings.append((keys_missing_value, 'Parameter must have a value.'))

    for vector_key in ('aoi_vector_path', 'land_polygon_vector_path'):
        try:
            if args[vector_key] not in ('', None):
                with utils.capture_gdal_logging():
                    vector = gdal.OpenEx(args[vector_key])
                    if vector is None:
                        warnings.append(
                            ([vector_key],
                             ('Parameter must be a path to an OGR-compatible '
                              'vector file.')))
        except KeyError:
            # neither of these vectors are required, so they may be omitted.
            pass

    if limit_to in ('bathymetry_path', None):
        with utils.capture_gdal_logging():
            raster = gdal.OpenEx(args['bathymetry_path'])
        if raster is None:
            warnings.append((['bathymetry_path'],
                             ('Parameter must be a path to a GDAL-compatible '
                              'raster on disk.')))

    if limit_to in ('wind_data_path', None):
        try:
            table_dict = utils.build_lookup_from_csv(args['wind_data_path'],
                                                     'REF')

            missing_fields = (set(['long', 'lati', 'lam', 'k', 'ref']) - set(
                table_dict.itervalues().next().keys()))
            if missing_fields:
                warnings.append((['wind_data_path'],
                                 ('CSV missing required fields: %s' %
                                  (', '.join(missing_fields)))))

            try:
                for ref_key, record in table_dict.iteritems():
                    for float_field in ('long', 'lati', 'lam', 'k'):
                        try:
                            float(record[float_field])
                        except ValueError:
                            warnings.append(
                                (['wind_data_path'],
                                 ('Ref %s column %s must be a number.' %
                                  (ref_key, float_field))))

                        try:
                            if float(ref_key) != int(float(ref_key)):
                                raise ValueError()
                        except ValueError:
                            warnings.append(
                                (['wind_data_path'],
                                 ('Ref %s ust be an integer.' % ref_key)))
            except KeyError:
                # missing keys are reported earlier.
                pass
        except IOError:
            warnings.append((['wind_data_path'], 'Could not locate file.'))
        except csv.Error:
            warnings.append((['wind_data_path'], 'Could not open CSV file.'))

    if limit_to in ('aoi_vector_path', None):
        try:
            if args['aoi_vector_path'] not in ('', None):
                with utils.capture_gdal_logging():
                    vector = gdal.OpenEx(args['aoi_vector_path'])
                    layer = vector.GetLayer()
                    srs = layer.GetSpatialRef()
                    units = srs.GetLinearUnitsName().lower()
                    if units not in ('meter', 'metre'):
                        warnings.append((['aoi_vector_path'],
                                         'Vector must be projected in meters'))
        except KeyError:
            # Parameter is not required.
            pass

    for simple_csv_key in ('global_wind_parameters_path',
                           'turbine_parameters_path'):
        try:
            csv.reader(open(args[simple_csv_key]))
        except IOError:
            warnings.append(([simple_csv_key], 'File not found.'))
        except csv.Error:
            warnings.append(([simple_csv_key], 'Could not read CSV file.'))

    if limit_to in ('number_of_turbines', None):
        try:
            num_turbines = args['number_of_turbines']
            if float(num_turbines) != int(float(num_turbines)):
                raise ValueError()
        except ValueError:
            warnings.append((['number_of_turbines'],
                             ('Parameter must be an integer.')))

    for float_key in ('min_depth', 'max_depth', 'min_distance', 'max_distance',
                      'foundation_cost', 'discount_rate', 'avg_grid_distance',
                      'wind_price', 'rate_change'):
        try:
            float(args[float_key])
        except ValueError:
            warnings.append(([float_key], 'Parameter must be a number.'))
        except KeyError:
            pass

    if limit_to in ('grid_points_path', None):
        try:
            table_dict = utils.build_lookup_from_csv(args['grid_points_path'],
                                                     'id')

            missing_fields = (set(['long', 'lati', 'id', 'type']) - set(
                table_dict.itervalues().next().keys()))
            if missing_fields:
                warnings.append((['grid_points_path'],
                                 ('CSV missing required fields: %s' %
                                  (', '.join(missing_fields)))))

            try:
                for id_key, record in table_dict.iteritems():
                    for float_field in ('long', 'lati'):
                        try:
                            float(record[float_field])
                        except ValueError:
                            warnings.append(
                                (['grid_points_path'],
                                 ('ID %s column %s must be a number.' %
                                  (id_key, float_field))))

                        try:
                            if float(id_key) != int(float(id_key)):
                                raise ValueError()
                        except ValueError:
                            warnings.append(
                                (['grid_points_path'],
                                 ('ID %s must be an integer.' % id_key)))

                        if record['type'] not in ('land', 'grid'):
                            warnings.append(
                                (['grid_points_path'],
                                 ('ID %s column TYPE must be either "land" or '
                                  '"grid" (case-insensitive)') % id_key))
            except KeyError:
                # missing keys are reported earlier.
                pass
        except KeyError:
            # This is not a required input.
            pass
        except IOError:
            warnings.append((['grid_points_path'], 'Could not locate file.'))
        except csv.Error:
            warnings.append((['grid_points_path'], 'Could not open CSV file.'))

    if limit_to in ('wind_schedule', None) and ('price_table' in args and
                                                args['price_table'] is True):
        try:
            table_dict = utils.build_lookup_from_csv(args['wind_schedule'],
                                                     'year')

            missing_fields = (set(['year', 'price']) - set(
                table_dict.itervalues().next().keys()))
            if missing_fields:
                warnings.append((['wind_schedule'],
                                 ('CSV missing required fields: %s' %
                                  (', '.join(missing_fields)))))

            try:
                year_list = []
                for year_key, record in table_dict.iteritems():
                    try:
                        if float(year_key) != int(float(year_key)):
                            raise ValueError()
                    except ValueError:
                        warnings.append(
                            (['wind_schedule'],
                             ('Year %s must be an integer.' % year_key)))
                    else:
                        year_list.append(year_key)

                    try:
                        float(record['price'])
                    except ValueError:
                        warnings.append(
                            (['wind_schedule'],
                             ('Price %s must be a number' % record['price'])))

                duplicate_years = set(
                    [year for year in year_list if year_list.count(year) > 1])
                if duplicate_years:
                    warnings.append(
                        (['wind_schedule'], "The following year(s) showed up "
                         "more than once: %s." % list(duplicate_years)))

            except KeyError:
                # missing keys are reported earlier.
                pass
        except IOError:
            warnings.append((['wind_schedule'], 'Could not locate file.'))
        except KeyError:
            warnings.append((['wind_schedule'], 'Key Undefined.'))
        except csv.Error:
            warnings.append((['wind_schedule'], 'Could not open CSV file.'))

    if limit_to is None:
        # Require land_polygon_vector_path if any of min_distance,
        # max_distance, or valuation_container have a value.
        try:
            if any((args['min_distance'] not in ('', None),
                    args['max_distance'] not in ('', None),
                    args['valuation_container'] is True)):
                if args['land_polygon_vector_path'] in ('', None):
                    warnings.append(
                        (['land_polygon_vector_path'],
                         'Parameter is required, but has no value.'))
        except KeyError:
            # It's possible for some of these args to be missing, in which case
            # the land polygon isn't required.
            pass

    return warnings
