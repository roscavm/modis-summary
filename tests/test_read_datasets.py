from modis_summary import read_datasets

from .data import TIFFILE


def test_get_year():
    year = read_datasets.get_year(TIFFILE[0])

    assert year == '2000'


def test_get_doy():
    doy = read_datasets.get_doy(TIFFILE[0])

    assert doy == '365'
