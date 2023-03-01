# -*- coding: utf-8 -*-
fhand = open('romeo.txt')
unique=[]
for word in fhand:
    word=word.rstrip()
    word=word.split()
    for w in word:
        if w not in unique:
            unique.append(w)
unique.sort()
print(unique)
