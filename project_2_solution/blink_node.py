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

import sys
import blink_utilities

from midas.node import BaseNode
from midas import utilities as mu


# Blink detector processing node
class BlinkNode(BaseNode):

    def __init__(self, *args):
        """ Initialize ECG node. """
        super().__init__(*args)

        # Append function handles to the metric_functions-list
        self.metric_functions.append(self.calculate_blinks)
        self.metric_functions.append(self.calculate_blinkrate)

    def calculate_blinks(self, x, fs=500):
        """ Calculate the number of blinks that occured in the specified
            time-window.
        """
        blinks = blink_utilities.find_blinks(x['data'][0], fs)
        number_of_blinks = blink_utilities.calculate_blinks(blinks)
        return number_of_blinks

    def calculate_blinkrate(self, x, fs=500):
        """ Calculate the blink-rate in the specified time-window
        """
        blinks = blink_utilities.find_blinks(x['data'][0], fs)
        number_of_blinks = blink_utilities.calculate_blinks(blinks)
        return number_of_blinks / (x['time'][0][0] - x['time'][0][-1])


# Run the node from command line
if __name__ == '__main__':
    node = mu.midas_parse_config(BlinkNode, sys.argv)
    if node:
        node.start()
        node.show_ui()
