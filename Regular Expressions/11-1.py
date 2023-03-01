# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:14:21 2023

@author: Lindean
"""
import re
print('$ python grep.py')
count=0
regular=input('Enter a regular expression:')
mail=open('mbox.txt')
#regex='.*'+regular+'.*'
for line in mail:
    #line=line.rstrip()
    if re.search(regular,line):
        count+=1

print('mbox.txt had ',count,' lines that matched ',regular)

"""
The following are from github open source, not by me.
import re

count = 0                               # Initialize variables

input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp)                # Regular Expressions are strings
fname = 'mbox.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    # Only counts if something was found
    if re.findall(reg_exp, line) != []:
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)
"""

    
    
