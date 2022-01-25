# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:29:00 2021

@author: Aungp
"""

v1 = 1/49 * 49
v2 = 1/51 * 51

print('v1=%.16f'%v1)
print('v2=%.16f'%v2)

a = 0.1; b = 0.2
computed = a + b
expected = 0.3
correct = computed == expected
print('Correct',correct)
print('a = %.17f\nb = %.17f\ncomputed = %.17f\nexpected = %.17f'%(a,b,computed,expected))