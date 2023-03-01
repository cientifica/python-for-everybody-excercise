# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:41:58 2023

@author: Lindean
"""

import socket, re
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
d=b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    d=d+data
mysock.close()
pos=d.find(b'\r\n\r\n')
print(d[pos:].decode())