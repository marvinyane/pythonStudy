import socket
import struct
import bluetec_pb2
import bluetec_evts

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

def transport_init(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))
    return sock

def send_data(sock, data):
    sock.send(data)

def waitEvent(sock, events):
    while 1 :
        data = sock.recv(1024) 
        if data: 
            obj = bluetec_pb2.OPCODE()
            obj.ParseFromString(data)
            if (len(events) == 0 or obj.opcode in events):
                return bluetec_evts.parseEvent(obj.opcode, data)
            else:
                continue
        else: 
            sock.close()
            break

