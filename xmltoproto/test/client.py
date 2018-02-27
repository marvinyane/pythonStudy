#! /usr/bin/python
import sys
import socket
import struct
import threading
import test_pb2

class Bdaddr():
    def __init__(self, uap, lap, nap):
        self.uap = uap
        self.lap = lap
        self.nap = nap

    def getStr(self):
        return struct.pack("BBBBBB", (self.uap >> 8) & 0xff,
                self.uap & 0xff,
                self.lap & 0xff,
                (self.nap >> 16) & 0xff,
                (self.nap >> 8 ) & 0xff,
                self.nap & 0xff)

class buffer():
    def __init__(self, buf):
        self.buf = buf

    def getStr(self):
        return struct.pack(len(self.buf)*'B', *self.buf)

class Client(threading.Thread): 
    def __init__(self,(sock)):
        threading.Thread.__init__(self) 
        self.sock = sock
        self.size = 1024 

    def run(self): 
        running = 1 
        while running: 
            data = self.sock.recv(self.size) 
            if data: 
                obj = test_pb2.OPCODE()
                obj.ParseFromString(data)
                print("%d %d " %(len(data), obj.opcode))
            else: 
                self.sock.close() 
                running = 0 

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6665))
    return sock

def send_data(sock, data):
    sock.send(data)

def BT_GEN_POWER_ON_REQ(sock, addr):
    obj = test_pb2.BT_GEN_POWER_ON_REQ_C()
    obj.opcode = 0x0001
    obj.local_addr = addr.getStr()
    send_data(sock, obj.SerializeToString())

if __name__ == '__main__':
    sock = create_socket()

    c = Client(sock)
    c.start()
    
    addr = Bdaddr(0x2b3c, 0x04, 0x000305)

    BT_GEN_POWER_ON_REQ(sock, addr)

    c.join()


