import datetime
import pathlib

import fiona
import rasterio
import rasterio.mask

from fiona.transform import transform_geom
from shapely.geometry import mapping, shape


def open_data(image, shape):
    """
    Open the images and read using rasterio.
    Parameters
    ----------
    image : Path
        Path to tiff image.
    shape : Path
        Path to shapefile.
    Returns
    -------
    A : np.ndarray
        3darray of length 1. Size dependant on input image.
    Raises
    -------
    ValueError
        If the input file contains more than one band.
    """
    with rasterio.open(image) as src0:
        crs = src0.crs
        bands = src0.count

    if bands != 1:
        raise ValueError(f'File not accepted. Only single band images allowed.')

    geom = _transform_vector(shape, crs)

    with rasterio.open(image) as src:
        data = rasterio.mask.mask(src, geom, all_touched=True, crop=True)[0]\
                       .astype(rasterio.float32)

    return data


def _transform_vector(point, crs):
    """Reads vector AOI bounds and reprojects to EPSG:4326. Returns bounds as shapely polygon.
    Parameters
    ----------
    infile : str
        Path to vector AOI.
    Returns
    -------
    shp : shapely object
        Infile AOI bounds as a shapely polygon object.
    Raises
    -------
    ValueError
        If the input shapefile contains more than one geometry.
    ValueError
        If the input file is not of an accepted file format.
    """

    vector_exts = ['.shp', '.geojson', '.json']
    ext = pathlib.Path(point).suffix

    if ext not in vector_exts:
        raise ValueError(f'File not accepted. Acceptable vector formats are {vector_exts}')

    with fiona.open(point, encoding='utf-8') as c:
        if len(c) > 1:
            raise ValueError('Shapefile contains multiple points. '
                             'Only single point shapefiles may be used as input.')

        transformed = transform_geom(c.crs.get("init"), str(crs), c[0]['geometry'])
        shp = shape(transformed)
        geom = [mapping(shp)]

        return geom


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
