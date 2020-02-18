import numpy as np


def summary(data):
    """
    Get summary statistics for the input image. Summary statistics included are:
    count, minimum, 25th percentiel, mean, median, 75th percentile, maximum, standard deviation.

    Parameters
    ----------
    image : Path
        Path to tiff image.
    shapefile : Path
        Path to shapefile.

    Returns
    -------
    summary_stats : dictionary
        Dictionary containing the year and day of acquisiton and summary statistics for the image.

    """

    count = np.count_nonzero(~np.isnan(data))
    minimum = np.nanmin(data)
    p25 = np.nanpercentile(data, 25)
    mean = np.nanmean(data)
    median = np.nanmedian(data)
    p75 = np.nanpercentile(data, 75)
    maximum = np.nanmax(data)
    stdev = np.nanstd(data)

    summary_stats = {'count': count,
                     'minimum': minimum,
                     '25th_percentile': p25,
                     'mean': mean,
                     'median': median,
                     '75th_percentile': p75,
                     'maximum': maximum,
                     'stdev': stdev}

    return summary_stats
