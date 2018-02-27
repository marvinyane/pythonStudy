#!/usr/bin/python3

import os
import sys
import parse_xml

types = {
        "u8" : "uint8",
        "u16" : "uint16",
        "u24" : "uint24",
        "u32" : "uint32",
        "str" : "uint8*",
        "buff" : "uint8*",
        "u8[]" : "uint8*",
        "bdaddr" : "bdaddr"
        }

def create_header(f_handler):
    f_handler.write("import bluetec_pb2\n")

def create_cmd(cmds):
    f_cmd = open('bluetec_cmds.py', 'w')
    create_header(f_cmd)

    f_cmd.write('import bluetec_tools\n\n')

    for cmd in cmds:
        type = cmd['name'].split('_')[-1]
        if type == 'REQ' or type == 'RES':
            f_cmd.write("def %s(sock" %(cmd['name']))
            for param in cmd['params']:
                f_cmd.write(" ,%s" %(param['name']))

            f_cmd.write('):\n')
            f_cmd.write("\tobj = bluetec_pb2.%s_C()\n" %(cmd['name']))
            f_cmd.write("\tobj.opcode = %s\n" %(cmd['opcode']))

            for param in cmd['params']:
                if param['type'].lower() in types:
                    if param['type'].lower() == 'bdaddr' or param['type'].lower() == 'buff':
                        f_cmd.write("\tobj.%s = %s.getStr()\n" %(param['name'], param['name']))
                    else:
                        f_cmd.write("\tobj.%s = %s\n" %(param['name'], param['name']))

            f_cmd.write("\tbluetec_tools.send_data(sock, obj.SerializeToString())\n")
    f_cmd.close()

def create_evt(cmds):
    f_evt = open('bluetec_evts.py', 'w')
    create_header(f_evt)

    f_evt.write("def parseEvent(opcode, data):\n")

    for cmd in cmds:
        type = cmd['name'].split('_')[-1]
        if type == 'CFM' or type == 'IND':
            f_evt.write("\tif opcode == %s:\n" %(cmd['opcode']))
            f_evt.write("\t\treturn %s(opcode, data)\n" %(cmd['name']))

    for cmd in cmds:
        type = cmd['name'].split('_')[-1]
        if type == 'CFM' or type == 'IND':
            f_evt.write("def %s(opcode, data):\n" %(cmd['name']))
            f_evt.write("\tobj = bluetec_pb2.%s_C()\n" %(cmd['name']))
            f_evt.write("\tobj.ParseFromString(data)\n")
            f_evt.write("\treturn obj\n")

    f_evt.close()

def create_message_dump(cmds):
    fh = open('bluetec_dump.py', 'w')
    fh.write('import sys\n')
    create_header(fh)

    fh.write('def DUMP_MESSAGE(obj):\n')
    for cmd in cmds:
        fh.write('\tif obj.opcode == %s:\n' %cmd['opcode'])
        fh.write('\t\tDUMP_%s(obj)\n' %cmd['name'])

    for cmd in cmds:
        fh.write('def DUMP_%s(obj):\n' % cmd['name'])
        fh.write("\tsys.stdout.write('%s')\n" % cmd['name'])
        for param in cmd['params']:
            if param['type'].lower() == 'bdaddr' or types[param['type'].lower()] == 'uint8*':
                fh.write("\tsys.stdout.write(' %s=%%s' %% obj.%s)\n" % (param['name'], param['name'].lower()))
            else:
                fh.write("\tsys.stdout.write(' %s=%%d' %% obj.%s)\n" % (param['name'], param['name'].lower()))
        
        fh.write("\tsys.stdout.write('\\n')\n")

    fh.close()


if __name__ == '__main__':
    file = sys.argv[1]
    if not os.path.exists(file):
        sys.exit(1)
    
    cmds = parse_xml.load_xml_file(file)

    create_cmd(cmds)
    create_evt(cmds)
    create_message_dump(cmds)

