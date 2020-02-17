# modis-summary

Summary statistics for an AOI from MODIS datasets.

## Installation

### 1. Miniconda Python

1. Download and install [Miniconda](https://conda.io/miniconda.html) (Python 3).
   If you already have Anaconda or Miniconda installed, you can skip this step.

2. Make sure that Miniconda is in the system environment variables under Path. Commonly under:
    ```
    C:\Users\<USER>\AppData\Local\Continuum\miniconda3\Scripts
    C:\Users\<USER>\AppData\Local\Continuum\miniconda3
    ```

### 2. The modis_summary environment

1. [Download the most recent environment.yml file](https://github.com/roscavm/modis-summary/raw/master/environment.yml) (right-click, `save-as`) and run:
    ```
    conda env create -f /path/to/environment.yml
    ```
   This creates the **modis_summary environment**

## Usage

After installation, the **modis_summary environment** will contain the `modis_summary` command-line interface.

#### 1. Activate the **modis_summary environment**
```
activate modis_summary
```

ALTERNATIVELY

```
conda activate modis_summary
```

#### 2. Get information about the `modis_summary` CLI with:
```
modis_summary --help
```
```
Usage: modis_summary [OPTIONS] COMMAND [ARGS]...

  MODIS Statistics Extraction Tool

Options:
  --help  Show this message and exit.

Commands:
  summary  Create a csv file containing the summary statistics for the...
```

### Individual Commands

The individual commands available within modis_summary are: `summary`

```
modis_summary summary --help
```
```
Usage: modis_summary summary [OPTIONS]

  Create a csv file containing the summary statistics for the timeseries at
  the chosen point. The following output statistics are generated for each
  year in the timeseries:

  YEAR - The year of acquisition for the image.
  DOY - The day of year of acquisition for the image.
  COUNT - The number of valid pixels within the area of interest.
  MINIMUM - The minimum value of a pixel within the area of interest.
  25TH_PERCENTILE - The 25th percentile value of all valid pixels within the area of interest.
  MEAN - The mean value of all valid pixels within the area of interest.
  MEDIAN - The median value of all valid pixels within the area of interest.
  75TH_PERCENTILE - The 75th percentile value of all valid pixels within the area of interest.
  MAXIMUM - The maximum value of a pixel within the area of interest.
  STDEV - The standard deviation value all valid pixels within the area of interest.

  Example use:

  modstats summary -i 'C:/DATA' -s 'C:/AOI/point_of_interest.shp' -o 'C:/OUTPUT/stats.csv'

Options:
  -i, --infolder PATH   Path to folder containing timeseries of hdf files.
                        e.g. C:/DATA  [required]
  -s, --shapefile FILE  Path to shapefile or geojson containing the area of
                        interest. e.g. C:/AOI/point_of_interest.shp
                        [required]
  -o, --outfile FILE    Path to output csv file where the output data will be
                        written.  e.g. C:/OUTPUT/stats.csv  [required]
  --help                Show this message and exit.
```
