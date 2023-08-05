# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

import fiona
from shapely.geometry import mapping, shape

from .main import Centerline
from .utils import get_ogr_driver, is_valid_geometry


def create_centerlines(src, dst, density=0.5):
    """
    Create centerlines and save the to an ESRI Shapefile.

    Reads polygons from the `src` ESRI Shapefile, creates Centerline
    objects with the specified `density` parameter and writes them to
    the `dst` ESRI Shapefile.

    Only Polygon features are converted to centerlines. Features of
    different types are skipped.

    Args:
        src (str): source ESRI Shapefile
        dst (str): destination ESRI Shapefile
        density (:obj:`float`, optional): the Centerline's density.
            Defaults to 0.5 (meters)

    Returns:
        None

    """
    try:
        DST_DRIVER = get_ogr_driver(filepath=dst)
    except ValueError:
        raise

    with fiona.Env():
        with fiona.open(src, mode='r') as source:
            SCHEMA = source.schema.copy()
            SCHEMA.update({'geometry': 'MultiLineString'})
            with fiona.open(
                    dst,
                    mode='w',
                    driver=DST_DRIVER.GetName(),
                    schema=SCHEMA,
                    crs=source.crs,
                    encoding=source.encoding) as destination:
                for record in source:
                    geom = record.get('geometry')
                    input_geom = shape(geom)

                    if not is_valid_geometry(geometry=input_geom):
                        continue

                    attributes = record.get('properties')
                    try:
                        centerline_obj = Centerline(
                            input_geom=input_geom,
                            interpolation_dist=density,
                            **attributes
                        )
                    except RuntimeError as err:
                        logging.warning(
                            "ignoring record that could not be processed: %s",
                            err
                        )
                        continue

                    centerline_dict = {
                        'geometry': mapping(centerline_obj),
                        'properties': {
                            k: v
                            for k, v in centerline_obj.__dict__.items()
                            if k in attributes.keys()
                        }
                    }

                    destination.write(centerline_dict)

    return None
