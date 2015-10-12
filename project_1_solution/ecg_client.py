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

import requests
import time
import sys


def request_hr(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"mean_hr", "channels":["ch0"], "time_window":[5], "arguments":[100]}'
    return round(requests.get(address + request).json()[0]['return'])


def request_rmssd(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"rmssd", "channels":["ch0"], "time_window":[300], "arguments":[100]}'
    return round(requests.get(address + request).json()[0]['return'])


def main(nodename):
    print('HEART-RATE'.ljust(15) + 'RMSSD')
    try:
        while True:
            hr_value = request_hr(nodename)
            rmssd_value = request_rmssd(nodename)
            print('{}'.format(hr_value).ljust(15) + '{}'.format(rmssd_value))
            time.sleep(2)
    except KeyboardInterrupt:
        print('\n\nQuitting!')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('ecg_client.py only takes 1 input argument (name of the node)!')
