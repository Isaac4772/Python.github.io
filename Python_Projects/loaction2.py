# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:04:17 2021

@author: Aungp
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--v0', '--initial_velocity', type=float, default = 0.0)
parser.add_argument('--s0', '--initial_position', type=float, default = 0.0)
parser.add_argument('--a', '--accleration', type=float, default = 0.0)
parser.add_argument('--t', '--time', type=float, default = 0.0)
args = parser.parse_args()
s0 = args.s0
v0 = args.v0
a = args.a
t = args.t
s = s0 + v0*t + 0.5*a*t*t
print(s)