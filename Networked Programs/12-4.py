# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:17:24 2023

@author: Lindean
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('p')
count=0
for tag in tags:
    count+=1
print("the number of <p> is",count)
