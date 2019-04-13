#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: mmxue
Created on April 13 2019
Be careful to put items in original
'''

import os
import numpy as np

def mixEpsilon(e1,e2):
  return e12 = sqrt(e1*e2)

def mixSigma(s1,s2):
  return s12 = (s1+s2)/2

try:
  infile = open(sys.argv[1],'r').readlines()
except:
  print('need one file')
  sys.exit()
 
outlines = []
n = len(infile)

for i in range(n):
  atomname_i = infile[i].strip().split()[0]
  epsilon_i = float(infile[i].strip().split()[1])
  sigma_i = float(infile[i].strip().split()[2])
  for j in range(i,n):
    atomname_j = infile[j].strip().split()[0]
    epsilon_j = float(infile[j].strip().split()[1])
    sigma_j = float(infile[j].strip().split()[2])
    newline = 'pair_coeff\t'+i+'\t'+j+'\t'+'lj/cut/coul/long\t'+'#\t'+atomname_i+'\t'+atomname_j
    outlines.append(newline)
    
outfile = open(sys.argv[1][:7]+'.params','w')
for line in outlines:
  outfile.write(line)
outfile.close()
print('done')
