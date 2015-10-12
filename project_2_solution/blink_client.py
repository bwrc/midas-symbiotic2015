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


def request_blink_count(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"calculate_blinks", "channels":["ch0"], "time_window":[5], "arguments":[500]}'
    return round(requests.get(address + request).json()[0]['return'])


def request_blink_rate(nodename):
    address = 'http://127.0.0.1:8080/'
    request = nodename + '/metric/{"type":"calculate_blinkrate", "channels":["ch0"], "time_window":[5], "arguments":[500]}'
    return requests.get(address + request).json()[0]['return']


def main(nodename):
    interval = 5
    try:
        while True:
            blink_count = request_blink_count(nodename)
            blink_rate = request_blink_rate(nodename)
            print('{} blinks in the past {} seconds. ({} blinks per second)'.format(blink_count, interval, blink_rate))
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\n\nQuitting!')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('blink_client.py only takes 1 input argument (name of the node)!')
