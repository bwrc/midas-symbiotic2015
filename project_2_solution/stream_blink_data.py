#!/usr/bin/env python3

# Andreas Henelius <andreas.henelius@ttl.fi>,
# Jari Torniainen <jari.torniainen@ttl.fi>
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
d_blink = read_data("data_blink.csv")

# make the data equally long

# create outlets
fs = 500.0
info_blink = lsl.StreamInfo('sim_blink', 'BLINK', 1, fs, 'float32', 'blink')
outlet_blink = lsl.StreamOutlet(info_blink)

# stream the data
print("streaming data")
i = 0
while True:
    outlet_blink.push_sample([d_blink[i]])
    time.sleep(1.0 / fs)
    i += 1
    if i >= len(d_blink):
        i = 0
