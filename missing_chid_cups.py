#!/usr/bin/python2

import fileinput
import numpy as np
from array import *
import csv
import sys

infile=sys.argv[1]
outfile=sys.argv[2]
dif_ind=0
indices=list()
acnt=[]
acid=list(range(001, 182))
acid.extend([220, 221, 222, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 358])
acid = [str(item).zfill(3) for item in acid]
cnt = []
cid = []
with open(infile) as inpf:
	for line in inpf:
		split = line.strip().split(' ',1)
		cnt.append(split[0])
		cid.append(split[1])
acnt=cnt

#for pcid, pcnt in zip(cid, cnt):
#	print pcid, pcnt
#print cid
#print acid
#print cnt
#print acnt

#dif_list = np.setdiff1d(cid,acid,assume_unique=True)

dif_list = [item for item in  acid if item not in cid]
for item in dif_list:
	dif_ind=[i for i, x in enumerate(acid) if x == item]
	indices.extend(dif_ind)

print range(len(indices))
for i in range(len(indices)):
	acnt.insert(indices[i],0)
#	print indices[i]

print dif_list
print indices
print acnt

print infile 
print outfile
with open(outfile, 'w') as outf:
	for pcid,pcnt in zip(acid, acnt):
		print >> outf, pcid, pcnt

#fileinput.close()

