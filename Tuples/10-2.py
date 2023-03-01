# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:53:37 2022

@author: Lindean
"""
d={}
mail=open('mbox-short.txt')
for line in mail:
    if not line.startswith('From'):continue
    line=line.rstrip()
    if len(line)<3:continue
    line=line.split(':')
    lines=line[0].split(' ')
    hour=lines[-1]
    if type(hour) is int: 
        d[hour]=d.get(hour,0)+1
    
lst=list(d.keys())
lst.sort()
for i in lst:
    print(i,d[i])