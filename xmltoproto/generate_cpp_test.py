#!/usr/bin/python3

import os
import sys
import string
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
    f_handler.write("#include <stdio.h>\n")
    f_handler.write("#include <stdlib.h>\n")
    f_handler.write("#include <string.h>\n")
    f_handler.write('#include "bluetec_hif.h"\n')
    f_handler.write('#include "bluetec_types.h"\n')
    f_handler.write('#include "bluetec_general_if.h"\n')
    f_handler.write('#include "bluetec.pb.h"\n')

    f_handler.write('using namespace std;\n')

    f_handler.write('extern bdaddr convertTobdaddr(string str);\n')


def create_cmd(cmds):
    create_header(f_cmd)
    f_cmd.write("void parseCmd(uint16 opcode, void* data, size_t len)\n{\nswitch (opcode)\n{\n")

    for cmd in cmds:
        type = cmd['name'].split('_')[-1]
        if type == 'REQ' or type == 'RES':
            f_cmd.write("case %s:\n{\n" %(cmd['name']))
            f_cmd.write("\t%s_C object;\n" %(cmd['name']))
            f_cmd.write("\tobject.ParseFromArray((const char*)data, len);\n")

            for param in cmd['params']:
                if param['type'].lower() in types:
                    if param['type'].lower() == 'bdaddr':
                        f_cmd.write("\tbdaddr %s = convertTobdaddr(object.%s());\n" %(param['name'],
                            param['name'].lower()))
                    elif types[param['type'].lower()] == 'uint8*':
                        f_cmd.write("\tuint8* %s = (uint8*)object.%s().c_str();\n" %(param['name'],
                            param['name'].lower()))
                    else:
                        f_cmd.write("\t%s %s = (%s)object.%s();\n" %(types[param['type'].lower()],
                        param['name'], types[param['type'].lower()], param['name'].lower()))

            func_name = string.capwords(cmd['name'], '_')
            func_name = ''.join(func_name.split('_'))
            f_cmd.write("\t%s(" %(func_name))
            start = True
            for param in cmd['params']:
                if start:
                    start = False
                else:
                    f_cmd.write(', ')

                f_cmd.write('%s' %param['name'])

            f_cmd.write(');\n')
            f_cmd.write("\tbreak;\n}\n")

    f_cmd.write("default:\nbreak;\n")
    f_cmd.write("}\n}\n")

def create_evt(cmds):
    create_header(f_evt)
    f_evt.write("void parseEvt(uint16 opcode, void* data)\n{\nswitch (opcode)\n{\n")

    for cmd in cmds:
        type = cmd['name'].split('_')[-1]
        if type == 'CFM' or type == 'IND':
            f_evt.write("case %s:\n{\n" %(cmd['name']))
            f_evt.write("\t%s_C object;\n" %(cmd['name']))
            f_evt.write("\t%s_T *prim = (%s_T*)data;\n" %(cmd['name'], cmd['name']))

            f_evt.write("object.set_opcode(%s);\n" %(cmd['name']))
            for param in cmd['params']:
                if param['type'].lower() in types:
                    if param['type'].lower() == 'bdaddr':
                        f_evt.write("object.set_%s((const char*)prim->%s.addr);\n" %(param['name'].lower(),
                            param['name'].lower()))
                    elif types[param['type'].lower()] == 'uint8*':
                        f_evt.write("object.set_%s((const char*)prim->%s);\n" %(param['name'].lower(),
                            param['name'].lower()))
                    else:
                        f_evt.write("object.set_%s(prim->%s);\n" %(param['name'].lower(), param['name'].lower()))

            f_evt.write("string str;\n")
            f_evt.write("object.SerializeToString(&str);\n")
            f_evt.write("SendOut(str);\n")


            f_evt.write("\tbreak;\n}\n")

    f_evt.write("default:\nbreak;\n")
    f_evt.write("}\n}\n")

if __name__ == '__main__':
    file = sys.argv[1]
    if not os.path.exists(file):
        sys.exit(1)
    
    cmds = parse_xml.load_xml_file(file)

    filename = ''.join(file.split('.')[:-1]).lower()
    
    # open status file, define the structure.
    f_cmd = open('parseCmd.cpp', 'w')
    f_evt = open('parseEvt.cpp', 'w')

    create_cmd(cmds)
    create_evt(cmds)

    f_cmd.close()
    f_evt.close()
