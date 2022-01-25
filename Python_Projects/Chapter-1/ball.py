# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:18:52 2021

@author: Aungp
"""

v0 = 5
t = 0.6
g = 9.81

y = v0*t - 0.5*g*t**2

print('v0=%f, t=%.4f, y=%.5f' %(v0, t, y))
print("""At t=%.2f s,
      a ball with initial velocity v0=%.2f m/s
      is located at %.3f m"""%(t,v0,y))