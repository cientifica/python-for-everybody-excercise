# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:15:59 2022

@author: Lindean
"""
d={}

mail=open('mbox-short.txt')
for line in mail:
    if not line.startswith('From'):continue
    line=line.split( )
    if len(line)<3:continue
    weekday=line[2]
    d[weekday]=d.get(weekday,0)+1
    log=line[1]
    d[log]=d.get(log,0)+1
    
    
print(d)
