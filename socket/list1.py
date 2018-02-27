import socket
import fcntl
import struct
import array
import platform

def all_interfaces():
    max_possible = 128  # arbitrary. raise if needed.
    bytes = max_possible * 32

    var1 = -1
    var2 = -1

    arch = platform.architecture()[0]
    if arch == '32bit':
        var1 = 32
        var2 = 32
    elif arch == '64bit':
        var1 = 16
        var2 = 40
    else:
        raise OSError("unknown architecture: %s" % arch)

    names = array.array('B', '\0' * bytes)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    outbytes = struct.unpack('iL', fcntl.ioctl(
                            s.fileno(),
                            0x8912,  # SIOCGIFCONF
                            struct.pack('iL', bytes, names.buffer_info()[0])
                ))[0]

    namestr = names.tostring()

    return [namestr[i:i+var1].split('\0', 1)[0] for i in range(0, outbytes, var2)]


names = all_interfaces()

for name in names:
    print(name)
