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


import numpy as np
from scipy import signal


# Define functions
def make_odd(x):
    if not (x % 2):
        x += 1
    return x


def moving_average(x, n):
    return np.convolve(x, np.ones(n)/n, mode='same')


def make_positive(x):
    x[x < 0] = 0
    return x


def cut_thr(x, q=95):
    thr = np.percentile(x, q=q)
    x[x < thr] = 0
    return x


def squarify(x):
    x[x < 0] = 0
    x[x > 0] = 1
    return x


def make_search_window(x, fs):
    ind_r = [i - fs/2 for i in np.where(np.diff(x) == 1)]
    ind_f = [i + fs/2 for i in np.where(np.diff(x) == -1)]
    return (ind_r, ind_f)


def find_peaks(x, ind_rise, ind_fall):
    peak_height = []
    peak_position = []

    for rise, fall in zip(ind_rise, ind_fall):
        rise = int(rise)
        fall = int(fall)
        peak_region = x[rise:fall]

        if peak_region:
            peak_height.append(max(peak_region))
            peak_position.append(np.argmax(peak_region) + rise - 1)
    return peak_position, peak_height


def find_blinks(x, fs, q=95):
    x_m = signal.medfilt(x, make_odd(fs))
    y = x - x_m
    y = make_positive(y)
    y = moving_average(y, fs / 10)
    y = cut_thr(y, q)
    y = squarify(y)
    tmp1 = make_search_window(y, fs)
    peaks = find_peaks(x, tmp1[0][0], tmp1[1][0])
    return peaks


def calculate_blinks(blinks):
    # TODO: Check if this even works
    return len(blinks[0])
