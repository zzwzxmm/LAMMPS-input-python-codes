#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Using pylab and numpy to plot figure of polymer-substrate interaction energy
'''

import numpy as np
import pylab as pl
import os

#-------------------------------------------------------------------------------
filename = 'Energy_peek-cu.txt'
file_energy = open(filename,mode='w')

# a = int(os.popen("ls *energy*txt -l | wc -l").read())
anneal_files = os.popen("ls *energy-???.txt").read().strip().split(sep='\n')
iso_files = os.popen("ls *energy-???-long.txt").read().strip().split(sep='\n')
decline_files = os.popen("ls *energy-???-Decline.txt").read().strip().split(sep='\n')
decline_files.sort(reverse=True)

for eachfile in anneal_files + iso_files + declines_files:
#--------------------aborted in order to use numpy and calculate std error
#   datafile = 'peek-cu-energy-300.txt'
#   temperature = float(datafile.split('.')[0].split('-')[3])
#
#   with open(datafile,'r') as f:
#       lines = 0
#       for line in f:
#           if line.startswith('#'):
#               print('pass')
#           else:
#               lines += 1
#               for i,data in enumerate(line.split()):
#                   sum[i] += float(data)
#   avgs = [s / lines for s in sums]
    datafile = eachfile
    temperature = float(datafile.split('.')[0].split('-')[3])
    datalist = []
    
    with open(datafile,'r') as f:
        for line in f:
            if line.startswith('#'):
                print('pass')
            else:
                b = float(line.split(sep=' ')[1])
                datalist.append(b)
    data_ave = np.mean(datalist)
    data_std = np.std(datalist)
    
    print(temperature,data_ave,data_std,sep='\t',file=file_energy)
    
file_energy.close()

data = np.loadtxt(filename)

pl.plot(data[::,0],data[::,1],'r-')
pl.xlabel('T (K)')
pl.ylabel('E (Kcal/mol)')
datax = data[:,0]; datax.sort()
datay = data[:,1]; datay.sort()
pl.xlim(datax[0],datax[-1])
pl.ylim(datay[0],datay[-1])

pl.show()
pl.savefig(str(filename)+'.png')


