# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:42:16 2021

@author: Aungp
"""
import sys
def read_C():
    try:
        C = float((sys.argv[1]))
    except IndexError:
        raise IndexError('You failed to provide the argument')
    except ValueError:
        raise ValueError('Your value %s is invalie!' % sys.argv[1])
    if C < -273.15:
        raise ValueError('C=%g is non-physical value' %C)
    return C

try:
    C = read_C()
except (IndexError, ValueError) as e:
    print(e)
    sys.exit(1)
F = (9.0/5) * C + 32
print(F)