import socket

print "start create socket..."
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "create socket ok"
sock.bind(('localhost',8001))
print "bind ok..."
sock.listen(10)
while True:
    print "start to accpet...\n"
    connection,address=sock.accept()
    try:
        connection.settimeout(5)
        buf=connection.recv(1024)
        if buf == '1':
            print "receive client data"
            connection.send('welcome to server')
        else:
            connection.send('bye bye !')
    except socket.timeout:
        print 'time out'
        connection.close()
