from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings
warnings.filterwarnings("ignore",
                        message='Matplotlib is building the font cache using fc-list. This may take a moment.')
warnings.filterwarnings("ignore",
                        message='The installed version of numexpr 2.4.4 is not supported in pandas and will be not be used')

import os
import sys

if sys.version_info[0] > 2:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve
    input = raw_input

import matplotlib
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    matplotlib.use('Agg')
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import glob
import gzip
import time
import ephem
import numpy as np
import scipy
import docopt
import pickle
import shutil
import socket
import datetime
import pylightcurve as plc

from scipy.interpolate import griddata
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy import interpolate
from sklearn.decomposition import FastICA, PCA
from astropy.io import fits as pf
