# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:09:39 2023

@author: Lindean
"""

import re
try:
    hand=input('Enter file:')
    hand=open(hand)
except:
    print('please enter the correct type of file')
count=0
suum=0
for line in hand:
    #line = line.rstrip()
    #print(line)
    #x = re.findall('.*rev=[0-9]+.*', line)
    x = re.findall('New Revision: ([0-9]+)', line)
    #print(x)
    if len(x) > 0:
        for i in range(len(x)):
            x[i]=int(x[i])
            suum+=x[i]
            count+=1
#print(suum)
#print(count)
print(suum//count)

"""import re

def average_revision(file_name):
    total = 0
    count = 0
    with open(file_name, "r") as f:
        for line in f:
            nums = re.findall('New Revision: ([0-9]+)', line)
            if len(nums) > 0:
                total += int(nums[0])
                count += 1
    return total // count

file_name = input("Enter file:")
print(average_revision(file_name))
"""