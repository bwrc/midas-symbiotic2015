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

import requests
import time
import sys


def request_current_app(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"current_app"}'
    return requests.get(address + request).json()[0]['return']


def request_idle_time(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"idle_time"}'
    return requests.get(address + request).json()[0]['return']


def main(nodename):
    try:
        while True:
            current_app = request_current_app(nodename)
            idle_time = request_idle_time(nodename)
            print('{}'.format(idle_time).ljust(15) + current_app)
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\nQuitting!")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('qs_client.py only takes 1 input argument (name of the node)!')
