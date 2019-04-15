#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: mmxue
Created on April 13 2019
Be careful to put items in original original atprm file in an order 
according to the atom type ids in lammps data file.
Atprm file format: atom_name / epsilon / sigma
              e.g.     cu        0.5      4.0
'''

import os, sys, math

#define functions to determine epsilon and sigma based on Lorentz method
# Epsilon
def mixEpsilon(e1,e2):
  e12 = math.sqrt(e1*e2)
  return e12
# Sigama
def mixSigma(s1,s2):
  s12 = (s1+s2)/2
  return s12

# Read atom types and original sigma and epsilon parameters
try:
  infile = open(sys.argv[1],'r').readlines()
except:
  print('Need one argv, atprm file')
  sys.exit()
 
outlines = []
n = len(infile)

# Generate the LJ parameters
for i in range(n):
  atomname_i = infile[i].strip().split()[0]
  epsilon_i = float(infile[i].strip().split()[1])
  sigma_i = float(infile[i].strip().split()[2])
# If not include LJ params between the same atoms, use i+1 instead of i in the next line.
  for j in range(i,n):
    atomname_j = infile[j].strip().split()[0]
    epsilon_j = float(infile[j].strip().split()[1])
    sigma_j = float(infile[j].strip().split()[2])
    m_epsilon = mixEpsilon(epsilon_i,epsilon_j)
    m_sigma = mixSigma(sigma_i,sigma_j)
    newline = 'pair_coeff\t'+'{:2d}'.format(i)+'\t'+'{:2d}'.format(j)+'\t'+'lj/cut/coul/long\t'\
    +'{:6.4f}'.format(m_epsilon)+'\t'+'{:6.4f}'.format(m_sigma)+'\t'+'#\t'+atomname_i+'\t'+atomname_j+'\n'
    outlines.append(newline)
    
# Write to a new file
outfile = open(sys.argv[1][:7]+'.params','w')
for line in outlines:
  outfile.write(line)
outfile.close()
print('Done. A new params file is written: {}.params'.format(sys.argv[1][:-7]))
