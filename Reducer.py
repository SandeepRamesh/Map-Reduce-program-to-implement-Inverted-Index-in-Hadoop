#! /usr/bin/env python
import os
import sys
inv={}

for line in sys.stdin:
    k,v=line.strip().split('\t')
    loc=inv.setdefault(k,[]).append(v)
	

for key,value in inv.items():
    c=dict()
    for item in value:
         if item in c:
             c[item]+=1
         else:
             c[item]=1
    sys.stdout.write("{0}\t{1}\n".format(key,c))
