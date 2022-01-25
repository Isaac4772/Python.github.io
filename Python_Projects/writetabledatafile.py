# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:56:49 2021

@author: Aungp
"""

data = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]
        ]

outfile = open('mydata.txt', 'w')
for row in data:
    for column in row:
        outfile.write('%4.0f' %column)
    outfile.write('\n')
outfile.close()

infile = open('mydata.txt', 'r')
for line in infile:
    print(line)
infile.close()