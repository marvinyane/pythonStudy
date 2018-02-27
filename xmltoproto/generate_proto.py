#!/usr/bin/python3

import os
import sys
import parse_xml

types = {
        "u8" : "uint32",
        "u16" : "uint32",
        "u24" : "uint32",
        "u32" : "uint32",
        "str" : "string",
        "buff" : "string",
        "u8[]" : "string",
        "bdaddr" : "string"
        }

def create_proto(fh, cmds):
    fh.write('message OPCODE{\n')
    fh.write('\trequired uint32 opcode = 1[default = 0xffff];\n}\n')
    for cmd in cmds:
        fh.write("message %s_C{\n"  %(cmd['name']))
        fh.write("\trequired uint32 opcode = 1 [default = %s];\n" %(cmd['opcode']))

        count = 1
        for param in cmd['params']:
            count = count + 1
            if param['type'].lower() in types:
                fh.write("\trequired %s %s = %d;\n" %(types[param['type'].lower()], param['name'], count))
            else:
                print("Error, unknown type %s - %s \n" %(param['type'], cmd['name']))

        fh.write("}\n")

if __name__ == '__main__':
    file = sys.argv[1]
    if not os.path.exists(file):
        sys.stderr.write("%s is not exist! \n" %(file))
        sys.exit(1)
    
    cmds = parse_xml.load_xml_file(file)

    filename = ''.join(file.split('.')[:-1]).lower()
    
    # open status file, define the structure.
    fh = open(filename+'.proto', 'w')
    create_proto(fh, cmds)

    fh.close()
