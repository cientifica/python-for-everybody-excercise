# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:12:53 2022

@author: Lindean
"""
wordsdict={}
words=open('words.txt')
for word in words:
    word=word.rstrip()
    w=word.split(" ")
    for i in w:
        if i not in wordsdict:
                wordsdict[i]=1
        else:
                wordsdict[i]+=1
print(wordsdict)
    