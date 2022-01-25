# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:29:07 2021

@author: Aungp
"""

f = open('rainfall.txt','w')
f.write("""Jan 81.2
Feb 63.2
Mar 70.3
Apr 55.7
May 53.0
Jun 36.4
Jul 17.5
Aug 27.5
Sep 68.9
Oct 117.7
Nov 1111.0
Dec 97.9
Year 792.9""")
f.close()

def extract_data(filename):
    infile = open(filename, 'r')
    months = []
    rainfall = []
    for line in infile:
        words = line.split()
        #words[0]:month, words[1]:rainfall
        months.append(words[0])
        rainfall.append(float(words[1]))
    infile.close()
    months = months[:-1]
    annual_avg = rainfall[-1]/12
    rainfall = rainfall[:-1]
    return months, rainfall, annual_avg

months, values, avg = extract_data('rainfall.txt')
print('The average rainfall for the months: ')
for month, value in zip(months, values):
    print(month, value)
print('the average rainfall for a year: ', avg)