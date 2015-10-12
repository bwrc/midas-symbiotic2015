#!/usr/env python3

# Andreas Henelius <andreas.henelius@ttl.fi>,
# Jari Torniainen <jari.torniainen@ttl.fi>
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


def request_lightlevel(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"mean_lightlevel", "channels":["ch0"], "time_window":[10]}'
    return round(requests.get(address + request).json()[0]['return'])


def main(nodename):
    interval = 5
    try:
        while True:
            lightlevel = request_lightlevel(nodename)
            lightlevel = 140 - lightlevel

            print('*' * lightlevel)
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\n\nQuitting!')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('iot_client.py only takes 1 input argument (name of the node)!')
