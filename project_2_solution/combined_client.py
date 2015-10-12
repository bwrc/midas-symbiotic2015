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

import time
import sys
from blink_client import request_blink_rate
from iot_client import request_lightlevel


def main(blink_nodename, iot_nodename):
    interval = 5
    try:
        while True:
            blink_count = request_blink_rate(blink_nodename)
            lightlevel = request_lightlevel(iot_nodename)
            lightlevel = 140 - lightlevel
            print('[' + '*' * lightlevel + ']Blinks per second: {}'.format(blink_count))

            time.sleep(interval)

    except KeyboardInterrupt:
        print('\n\nQuitting!')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('combined_client.py only takes 2 input argument (name of the blink node and the name of the iot node)!')
