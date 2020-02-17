import datetime
import pathlib

import fiona
import rasterio
import rasterio.mask

from fiona.transform import transform_geom
from shapely.geometry import mapping, shape


def get_doy(image):
    """
    Get the acquisition day of year of an input image based on the filename.

    Parameters
    ----------
    image : Path
        Path to tiff image.

    Returns
    -------
    doy : str
        Acquistiion day of year as string.

    """
    filepath = pathlib.Path(image)
    basename = filepath.name
    doy = datetime.datetime.strptime(basename[0:8], '%Y%m%d').timetuple().tm_yday

    return doy


def get_year(image):
    """
    Get the acquisition year of the image based on the filename.

    Parameters
    ----------
    image : Path
        Path to tiff image.

    Returns
    -------
    year : str
        Acquistiion year as string.

    """
    filepath = pathlib.Path(image)
    basename = filepath.name
    year = basename[0:4]

    return year


def open_data(image, shapefile):
    """
    Open the image and read using rasterio.

    Parameters
    ----------
    image : Path
        Path to tiff image.
    shapefile : Path
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

    geom = _transform_vector(shapefile, crs)

    with rasterio.open(image) as src:
        data = rasterio.mask.mask(src, geom, all_touched=True, crop=True)[0]\
                       .astype(rasterio.float32)

    return data


def _transform_vector(shapefile, crs):
    """Reads vector AOI bounds and reprojects to desired crs. Returns bounds as shapely polygon.

    Parameters
    ----------
    shapefile : Path
        Path to vector AOI.
    crs : rasterio CRS string
        CRS to transform to.

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
    ext = pathlib.Path(shapefile).suffix

    if ext not in vector_exts:
        raise ValueError(f'File not accepted. Acceptable vector formats are {vector_exts}')

    with fiona.open(shapefile) as c:
        if len(c) > 1:
            raise ValueError('File contains multiple features. '
                             'Only single feature files may be used as input.')

        transformed = transform_geom(c.crs.get("init"), str(crs), c[0]['geometry'])

    shp = shape(transformed)
    geom = [mapping(shp)]

    return geom
