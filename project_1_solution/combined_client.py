#!/usr/env python3

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
import sys
from ecg_client import request_hr
from qs_client import request_current_app


def main(ecg_nodename, qs_nodename):
    data = {}
    print('APPLICATION'.ljust(15) + 'MEAN HEART RATE')
    try:
        while True:
            hr_value = request_hr(ecg_nodename)
            current_app = request_current_app(qs_nodename)
            if current_app in data.keys():
                data[current_app] = (data[current_app][0] + hr_value,
                                     data[current_app][1] + 1)
            else:
                data[current_app] = (hr_value, 1)

            for app_name in data.keys():
                average_hr = round(data[app_name][0] / data[app_name][1])
                print(app_name.ljust(15) + '{} BPM'.format(average_hr))
            print('-' * 30)
            time.sleep(2)
    except KeyboardInterrupt:
        print('\n\nQuitting!')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('combined_client.py only takes 2 input argument (name of the ecg node and the name of the qs node)!')
