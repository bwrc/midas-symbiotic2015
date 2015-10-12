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
d_iot = read_data("data_iot.csv")

# make the data equally long

# create outlets
fs = 10.0
info_iot = lsl.StreamInfo('iot', 'IOT', 1, fs, 'float32', 'iot')
outlet_iot = lsl.StreamOutlet(info_iot)

# stream the data
print("streaming data")
i = 0
while True:
    outlet_iot.push_sample([d_iot[i]])
    time.sleep(1.0 / fs)
    i += 1
    if i >= len(d_iot):
        i = 0
