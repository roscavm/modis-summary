import click

@click.group()
def cli():
    """MODIS Statistics Extraction Tool"""
    pass


@cli.command()
@click.option('-i', '--infolder', type=click.Path(dir_okay=True, exists=True), required=True,
              help='Path to folder containing timeseries of hdf files. e.g. C:/DATA')
@click.option('-s', '--shapefile', type=click.Path(dir_okay=False, exists=True), required=True,
              help='Path to shapefile or geojson containing the area of interest. '
              'e.g. C:/AOI/point_of_interest.shp')
@click.option('-o', '--outfile', type=click.Path(dir_okay=False, exists=False), required=True,
              help='Path to output csv file where the output data will be written. '
              ' e.g. C:/OUTPUT/stats.csv')

def summary(**kwargs):
    """Create a csv file containing the summary statistics for the timeseries at the chosen point.
    The following output statistics are generated for each year in the timeseries:

    YEAR - The year of acquisition for the image.
    DOY - The day of year of acquisition for the image.
    COUNT - The number of valid pixels within the area of interest.
    MIN - The minimum value of a pixel within the area of interest.
    25TH_PERCENTILE - The 25th percentile value of all valid pixels within the area of interest.
    MEAN - The mean value of all valid pixels within the area of interest.
    MEDIAN - The median value of all valid pixels within the area of interest.
    75TH_PERCENTILE - The 75th percentile value of all valid pixels within the area of interest.
    MAX - The maximum value of a pixel within the area of interest.
    SD - The standard deviation value all valid pixels within the area of interest.

    Example use:

    modstats summary -i 'C:/DATA' -s 'C:/AOI/point_of_interest.shp' -o 'C:/OUTPUT/stats.csv'
    """
    from modis_summary import write_csv
    write_csv.main(**kwargs)
