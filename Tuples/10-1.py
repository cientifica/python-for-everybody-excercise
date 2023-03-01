# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:22:14 2022

@author: Lindean
"""

d={}
ma=None
maxmessage=None
mail=open('mbox-short.txt')
for line in mail:
    if not line.startswith('From'):continue
    line=line.rstrip()
    line=line.split(' ')
    if len(line)<3:continue
    log=line[1]
    d[log]=d.get(log,0)+1
    """if ma==None or ma<d[log]: 
        ma=d[log]
        maxmessage=log"""
#print(d)
#print(maxmessage,ma)
t=()
lst=[]
for i in d:
    t=(i,d[i])
    lst.append(t)
lst.sort(reverse=True)
for j in lst:
    if ma==None or ma<j[1]:
        ma=j[1]
        maxmessage=j[0]
print(maxmessage,ma)
