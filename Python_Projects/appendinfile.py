# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:50:19 2021

@author: Aungp
"""
f = open('test2.txt', 'a')
f.write("""This is first line
This is second line
this is third line""")
f.close()

infile = open('test2.txt', 'r')
for line in infile:
    print(line)
infile.close()