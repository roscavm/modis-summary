import os
import glob

here = os.path.abspath(os.path.dirname(__file__))

TIFFILES = glob.glob(os.path.join(here, '*.tif'))

print(TIFFILES)