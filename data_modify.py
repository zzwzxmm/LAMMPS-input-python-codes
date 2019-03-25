#!/bin/env python3
# -*- coding: utf-8 -*-

import sys

#modify the charges
def modify_charge(l,l_b,l_a):
    '''
    Modifying the charge of certain atoms of lammps data file from EMC software...
    '''
    f,i = float,int
    l_modified = l
    l,l_b,l_a = l.split(),l_b.split(),l_a.split()
    options = {
        'n'  : -0.385,
        'h'  : 0.3,
        'os' : -0.33,
        'ca' : 0.0,
        'cd' : 0.0,
        'c'  : 0.51,
        'c34': 0.25,
        'c32': 0.06,
        'o'  : -0.43,
        'cu' : 0.0,
        'c21': 0.25,
        'c2' : 0.0
    }
    if len(l) == 9 and len(l_a) == 9 and len(l_b) == 9:
        option = l[-1]
        l[3],nextline = options[option],'\n'
        l_t = i(l[0]),i(l[1]),i(l[2]),f(l[3]),f(l[4]),f(l[5]),f(l[6]),l[7],l[8]
        l = list(l_t)
        if (l_b[-1] == 'cu' or l_a[-1] == 'c32) and l[-1] == 'os':
            l[3] = -0.5
            l = '{0:8d}{1:8d}{2:4d}{3:8.4f}{4:15.10f}{5:15.10f}{6:15.10f}   {7}  {8:5s}{9}'.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],nextline)
            l_modified = ''.join(l)
        else:
            l = '{0:8d}{1:8d}{2:4d}{3:8.4f}{4:15.10f}{5:15.10f}{6:15.10f}   {7}  {8:5s}{9}'.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],nextline)
            l_modified = ''.join(l)
    return l_modified
   
# process lmp data
try:
    infile = open(sys.argv[1],'r').readlines()
except:
    print('First command-line argument is not a proper data file.')
    sys.exit()
    
outlines = []
outlines.append(infile[0])
while len(infile) >= 3:
    sl_b = infile[0]
    sl = infile[1]
    sl_a = infile[2]
    outlines.append(modify_charges(sl,sl_b,sl_a))
    infile.pop(0)
outlines.append(infile[1])

# write a new file
outfile = open(sys.arge[1][:-5]+'_charge-oplsua.data','w')
for line in outlines:
    outfile.write(line)
outfile.close()

print('A file with modified charges has been written: {0}_charge-oplsua.data'.format(sys.argv[1][:-5]))
