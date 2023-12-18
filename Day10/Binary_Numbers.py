#!/bin/python

import sys

n = int(input().strip())
binary = str(bin(n))
tot=0
tmp=0
for i in binary:
    if i=='1':
        tmp+=1
    else:
        tot=max(tot,tmp)
        tmp=0
tot=max(tot,tmp)
print(tot)
