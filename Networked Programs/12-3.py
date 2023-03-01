# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:38:31 2023

@author: Lindean
"""
"""
import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup

url=input('Enter-')
doc=urllib.request.urlopen(url)
count=0
for line in doc:
    words=line.decode().split()
    for word in words:
        for w in word:
            count+=1
            if count==3001:
                point=words.index(word)
                p=point.index(w)
                print()
    if count>3000:
        continue
    print(line.decode())"""
import urllib.request

# specify the URL
url = input('Enter-')

# open the URL and retrieve the document
response = urllib.request.urlopen(url)

# read the document contents
contents = response.read()

# decode the contents to a string
contents = contents.decode()

# display up to 3000 characters
print(contents[:3000])

# count the overall number of characters in the document
print("Number of characters:", len(contents))
