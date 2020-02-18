import csv
import pathlib

from modis_summary import get_stats, read_datasets


def main(infolder, shapefile, outfile):
    """
    Write a csv file containing the summary statistics.

    Parameters
    ----------
    infolder : Path
        Path to folder containing all the required .tif image.
    shapefile : Path
        Path to shapefile.
    outfile : Path
        Path to desired output csv file.

    """
    images = pathlib.Path(infolder).glob('*.tif')
    csv_columns = ['year', 'doy', 'count', 'minimum', '25th_percentile', 'mean', 'median',
                   '75th_percentile', 'maximum', 'stdev']
    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for i in images:
            data = read_datasets.open_data(i, shapefile)
            year = read_datasets.get_year(i)
            doy = read_datasets.get_doy(i)
            stats = get_stats.summary(data)
            stats['year'] = year
            stats['doy'] = doy
            writer.writerow(stats)
