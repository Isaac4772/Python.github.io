# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:38:06 2021

@author: Aungp
"""

from math import sin, cos, pi
x = pi/4
value1 = sin(x)**2 + cos(x)**2
print (int(value1))

v0 = 3 #m/s
t = 1 #s
a = 2 #*m/s**2
s = v0*t + 0.5*a*t**2
print(s)

a = 3.3; b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b +b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print('First equation: %g = %g'%(eq1_pow, eq1_sum))
print('Second equation: %g = %g'%(eq2_pow,eq2_sum))
