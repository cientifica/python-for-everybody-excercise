# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:37:54 2022

@author: Lindean
"""
d={}
mail=open('mbox-short.txt')
for line in mail:
    if not line.startswith('From'):continue
    line=line.rstrip()
    line=line.split(' ')
    name=line[1].split('@')
    domain=name[1]
    d[domain]=d.get(domain,0)+1
print(d)