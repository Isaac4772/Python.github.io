# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:51:01 2021

@author: Aungp
"""

v0 = 3; t = 0.6; g = 9.81
position = v0*t - 0.5*g*t*t
velocity = v0 - g*t
print('position',position,'velocity',velocity)
print('position=%.4f,velocity=%.4f'%(position,velocity))