import os
import glob

here = os.path.abspath(os.path.dirname(__file__))

TIFFILE = glob.glob(os.path.join(here, '*.tif'))
