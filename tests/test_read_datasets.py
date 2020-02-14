from modis_summary import read_datasets

from .data import TIFFILES


def test_get_years():
    years = read_datasets._get_years(TIFFILES)

    assert years == [2000, 2003]


def test_get_doys():
    doys = read_datasets._get_doys(TIFFILES)

    assert doys == [365, 1]
