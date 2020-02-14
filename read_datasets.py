import datetime
import os

import geopandas as gpd
import numpy as np
import rasterio
import rasterio.mask

from calendar import isleap

def open_data(images, geom, year):
    """
    Open the images and read using rasterio.
    Parameters
    ----------
    images : list
        List of images.
    geom : shapely mapping(object)
        Shapely map object to use as mask.
    year: int
        Year of acquisiton.
    Returns
    -------
    A : np.ndarray
        3darray of length 365 or 366 depending if leap year or not. Size dependant on input images.
    """
    for idx, i in enumerate(images):
        if idx == 0:
            with rasterio.open(i) as src0:
                data = rasterio.mask.mask(src0, geom, all_touched=True, crop=True)[0].astype(rasterio.float32)

        else:
            with rasterio.open(i) as src:
                read_d = rasterio.mask.mask(src, geom, all_touched=True, crop=True)[0].astype(rasterio.float32)
                data = np.vstack((data, read_d))

    doys = _get_doys(images)

    if isleap(year):
        A = np.empty((366, data.shape[1], data.shape[2]))
    else:
        A = np.empty((365, data.shape[1], data.shape[2]))

    A[:] = np.nan

    for i, d in enumerate(doys):
        A[int(d-1)] = data[i]

    return A


def read_shapefile(infile):
    """
    Read the input shapefile as gpd dataframe indexed on the 'COUNTRY' field.
    Parameters
    ----------
    infile : os.PathLike
        Path to shapefile.
    Returns
    -------
    shapefile : gpd.geodataframe.GeoDataFrame
        Shapefile as geopandas geodataframe.
    """
    shapefile = gpd.read_file(infile)

    return shapefile


def _get_doys(images):
    """
    Get the acquisition days of year for a list of input images.
    Parameters
    ----------
    images : list
        List of paths for all images.
    Returns
    -------
    doys : list
        List of floats with acquistiion doy.
    """
    doys = []

    for i in images:
        doy = datetime.datetime.strptime(os.path.basename(i)[0:8], '%Y%m%d').timetuple().tm_yday
        doy = float(doy)
        doys.append(doy)

    return doys


def _get_years(images):
    """
    Get the acquisition years based on the filename of images in the input list.
    Parameters
    ----------
    images : list
        List of images.
    Returns
    -------
    years : list
        List of years are ints.
    """
    years = []

    for i in images:
        y = int(os.path.basename(i)[0:4])
        if y not in years:
            years.append(y)

    return sorted(years)
