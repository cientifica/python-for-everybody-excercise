# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:09:02 2022

@author: Lindean
"""

def printnumber():
    try:
        while True:
            global total
            global count
            n=input('enter a number')
            if (n=='done'):
                print(total,count,total/count)
            else:
                n=int(n)
                total+=n
                count+=1
    except:
        print('Invalid input')
        printnumber()
total=0
count=0
printnumber()
