from setuptools import setup, find_packages

setup(
    name='modis_summary',
    version='0.1.0',
    description='Create summary statistics from a timeseries of MODIS datasets',
    author='Mike Rosca',
    author_email='roscavm@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        modis_summary=modis_summary.cli:cli
    '''
)