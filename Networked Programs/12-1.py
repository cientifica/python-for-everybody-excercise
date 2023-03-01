# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:02:48 2023

@author: Lindean
"""
import socket

url = input("Enter a URL: ")

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
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()
except:
    print("Invalid URL or Error Occured")
