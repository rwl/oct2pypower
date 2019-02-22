# Copyright 2019 Richard Lincoln

import logging

from oct2py import Oct2Py

logging.basicConfig(level=logging.INFO, format='%(message)s')

mp = Oct2Py(logger=logging.getLogger())
mp.addpath("/usr/local/matpower")
