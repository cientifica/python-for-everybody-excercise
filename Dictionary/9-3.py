# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:30:56 2022

@author: Lindean
"""
for i in range(2):
    d={}
    ma=None
    maxmessage=None
    try:
        mail=input('Enter a file name:')
    except:
        print('please enter the valid file')
    mail=open(mail)
    for line in mail:
        if not line.startswith('From'):continue
        line=line.rstrip()
        line=line.split(' ')
        if len(line)<3:continue
        log=line[1]
        d[log]=d.get(log,0)+1
        if ma==None or ma<d[log]: 
            ma=d[log]
            maxmessage=log
    #print(d)
    print(maxmessage,ma)
