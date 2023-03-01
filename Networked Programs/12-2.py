# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:30:55 2023

@author: Lindean
"""

import socket

url = input("Enter a URL: ")
count=0
try:
    url_parts = url.split('/')
    host = url_parts[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        #print(data)
        count+=len(data)
        if len(data) < 1:
            break
        elif count>3000:
            continue
        print(data.decode(), end='')
    mysock.close()
    print("tatal character",count)
except:
    print("Invalid URL or Error Occured")
