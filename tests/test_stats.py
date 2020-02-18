import numpy as np

from modis_summary import get_stats

DATA = np.ones((1, 10, 10))


def test_summary():
    stats = get_stats.summary(DATA)

    count = stats['count']
    minimum = stats['minimum']
    mean = stats['mean']
    maximum = stats['maximum']

    assert (count, minimum, mean, maximum) == (100, 1, 1, 1)
