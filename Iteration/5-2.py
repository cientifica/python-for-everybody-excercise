# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:41:21 2022

@author: Lindean
"""

def printnumber():
    try:
        while True:
            global total
            global count
            global num
            global inimin
            global inimax
            n=input('enter a number')
            if (n=='done'):
                for i in num:
                   if inimin==None or inimin>i:
                       inimin=i
                for j in num:
                   if inimax==None or inimax<i:
                       inimax=j
                print(total,count,inimin,inimax)
            else:
                n=int(n)
                total+=n
                count+=1
                num.append(n)
    except:
        print('Invalid input')
        printnumber()
total=0
count=0
num=[]
inimin=None
inimax=None
printnumber()