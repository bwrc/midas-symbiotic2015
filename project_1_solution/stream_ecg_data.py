#!/usr/bin/env python3

# Jari Torniainen <jari.torniainen@ttl.fi>
# Andreas Henelius <andreas.henelius@ttl.fi>,
# Finnish Institute of Occupational Health
# Copyright 2015
#
# This code is released under the MIT license
# http://opensource.org/licenses/mit-license.php
#
# Please see the file LICENSE for details

import time
import pylsl as lsl


def read_data(fname):
    data = open(fname, "r").readlines()
    data = [float(i.strip()) for i in data]
    return data


# read the data
d_ecg = read_data("data_ecg.csv")

# make the data equally long

# create outlets
fs = 500.0
info_ecg = lsl.StreamInfo('sim_ecg', 'ECG', 1, fs, 'float32', 'ecg123')
outlet_ecg = lsl.StreamOutlet(info_ecg)

# stream the data
print("streaming data")
i = 0
while True:
    outlet_ecg.push_sample([d_ecg[i]])
    time.sleep(1.0 / fs)
    i += 1
    if i >= len(d_ecg):
        i = 0
