# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:17:14 2021

@author: Aungp
"""

f = open('tmp.txt','w')
f.write("""Lineof 1
Lineof 2
Lineof 3
Lineof 4
""")
f.close()

infile = open('tmp.txt','r')
for line in infile:
    split_line = line.split('e')
    print(split_line)
    print(line)
    #lines = infile.readlines()
    #print(lines)