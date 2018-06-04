#!/usr/bin/python 

import socket 
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('116.62.18.190', 8001))
sock.send('1')
print sock.recv(1024)
sock.close()
