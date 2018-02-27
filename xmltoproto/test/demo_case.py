#! /usr/bin/python
import sys
from bluetec_cmds import *
from bluetec_tools import *
from bluetec_dump import *

if __name__ == '__main__':
    t = transport_init(6665)

    addr = Bdaddr(0x2b3c, 0x04, 0x000305)
    BT_GEN_POWER_ON_REQ(t, addr)

    obj = waitEvent(t, (0x8001,))

    DUMP_MESSAGE(obj)

    if obj.status != 0:
        print("power on failed!")
        sys.exit(1)

    
    BT_GEN_SET_LOCAL_NAME_REQ(t, 7, "marvin")
    waitEvent(t, (0x800B,))

    DUMP_MESSAGE(obj)

    if obj.status != 0:
        print("set local name error!")
    
    BT_GEN_SET_LOCAL_MODE_REQ(t, 1, 1, 1)
    waitEvent(t, (0x800F,))

    DUMP_MESSAGE(obj)

    if obj.status != 0:
        print("set local mode error!")

    while 1:
        sys.sleep(1)
