# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:02:43 2021

@author: Aungp
"""

infile = open('data.txt', 'r')
lines = infile.readLines()
print(lines)
sum = 0
for line in infile:
    number = float(line)
    sum += number
    #print(line)
print('Total is : %g' %sum)
mean = sum/len(lines)
print('Mean is : %f'%mean)
infile.close();