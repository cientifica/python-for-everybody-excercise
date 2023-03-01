# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:58:27 2022

@author: Lindean
"""
import os

os.chdir('C:\\Users\\Lindean\\Documents\\presentation')
from string import digits
import string
mail=open('mbox-short.txt')
counts={}
for line in mail:
    line=line.rstrip()
    line=line.translate(line.maketrans(' ',' ',string.punctuation))
    line=line.translate(line.maketrans(' ',' ',digits))
    line=line.translate(line.maketrans(' ',' ','\t'))
    line=line.lower()
    words=line.split(' ')
    for word in words:
        for w in word:
            counts[w]=counts.get(w,0)+1
lst=[]
for key, val in list(counts.items()):
    lst.append((key,val))
lst=sorted(lst,key=lambda x:x[1],reverse=True)
print(lst)
    