#! /bin/python

import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
try:
    s.connect("python_test_socket")
except socket.error, msg:
    print msg
    sys.exit(1)

try:
    print "start send data"
    s.send("hello, this is python")

    print "start receive data"
    data = s.recv(16)
    print data

finally:
    print "close socket"
    s.close()

    
