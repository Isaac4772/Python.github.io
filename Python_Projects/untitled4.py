# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:43:34 2021

@author: Aungp
"""

from math import log as ln

def present_amount(A0, p, n):
    return A0*(1+p/(360.0*100))**n

def initial_amount(A, p, n):
    return A*(1+p/(360.0*100))%(-n)

def days(A0, A, p):
    return ln(A/A0)/ln(1+)