#! /usr/bin/python
import socket
import getnifs

nifs = getnifs.get_network_interfaces()

for ni in nifs:
    print(ni.name)


