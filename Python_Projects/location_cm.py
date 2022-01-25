# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:58:00 2021

@author: Aungp
"""

import sys
s0 = float(sys.argv[1])
v0 = float(sys.argv[2])
a = float(sys.argv[3])
t = float(sys.argv[4])
s = s0 + v0*t + 0.5*a*t*t
print(s)