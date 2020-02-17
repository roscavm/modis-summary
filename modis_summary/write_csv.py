import pathlib
import csv

import get_stats

i = r'D:\stats_tests\i_tests'
s = r'D:\stats_tests\shapefiles\single_polygon.shp'
o = r'D:\stats_tests\shapefiles\single_polygon.csv'


def main(infolder, shapefile, outfile):
    """
    Get summary statistics for the input image.
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
        Summary statistics included are:
        count, minimum, 25th perce
    """
    images = pathlib.Path(infolder).glob('*.tif')
    csv_columns = ['year', 'doy', 'count', 'minimum', '25th_percentile', 'mean', 'median',
                   '75th_percentile', 'maximum', 'stdev']
    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for i in images:
            stats = get_stats.summary(i, shapefile)
            writer.writerow(stats)

main(i, s, o)