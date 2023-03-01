# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:57:26 2022

@author: Lindean
"""

a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'
j='j'
k='k'
l='l'
m='m'
n='n'
o='o'
p='p'
q='q'
r='r'
s='s'
t='t'
u='u'
v='v'
w='w'
x='x'
y='y'
z='z'
holiday='thanksgiving'
alph=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
count=[0]*26
for i in holiday:
    if i in alph:
        count[alph.index(i)]+=1
print(count)