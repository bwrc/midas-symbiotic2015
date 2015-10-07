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

from midas.node import BaseNode
from midas import utilities as mu
import numpy


# IoT light-level processing node
class IoTNode(BaseNode):

    def __init__(self, *args):
        """ Initialize ECG node. """
        super().__init__(*args)

        # Append function handles to the metric_functions-list
        self.metric_functions.append(self.mean_lightlevel)

    def mean_lightlevel(self, x):
        """ Get the mean light level of the specified time-window from the
            sensor
        """
        return numpy.mean(x['data'][0])


# Run the node from command line
if __name__ == '__main__':
    node = mu.midas_parse_config(IoTNode, sys.argv)
    if node:
        node.start()
        node.show_ui()
