#! /usr/bin/python

import os
import sys
import parse_xml

types = {
        "u8" : "uint8",
        "u16" : "uint16",
        "u24" : "uint24",
        "u32" : "uint32",
        "str" : "string",
        "buff" : "uint8*",
        "bdaddr" : "bdaddr"
        }

names = {
        "GEN" : "GM",
        "CM"  : "CM",
        "HFP" : "HM",
        "AV"  : "AM",
        "PBDL" : "PM",
        "SPP" : "SM",
        "MSG" : "MM",
        "PAN" : 'PM',
        }

tags = {
        "REQ" : "CMD",
        "CFM" : "ACK",
        "IND" : "EVT",
        "RES" : "RES"
        }

if __name__ == '__main__':
    file = sys.argv[1]
    if not os.path.exists(file):
        sys.exit(1)

    fh = open("test.js", 'w')

    cmds = parse_xml.load_xml_file(file)

    fh.write('var cmds = [\n')
    for cmd in cmds:
        fh.write('{')

        old = cmd['name'].split('_')
        new = ['WL']
        new.append(names[old[1]])
        for o in old[2:-1]:
            new.append(o)
        new.append(tags[old[-1]])

        new_name = '_'.join(new)

        fh.write('"name":"%s",' % new_name)
        fh.write('"opcode":"%s",' % cmd['opcode'])
        fh.write('"func":"%s",' % cmd['function'].replace('"', '').replace("\n", " "))

        fh.write('"params":[')

        for param in cmd['params']:
            fh.write('{')
            fh.write('"name":"%s",' % param['name'])
            fh.write('"type":"%s",' % types[param['type']])
            fh.write('"mean":"%s",' % param['meaning'].replace('"', '').replace("\n", " ").encode('utf-8'))
            fh.write('},')

        
        fh.seek(-1, os.SEEK_END)
        fh.write(']')

        fh.write('},\n')
    fh.seek(-1, os.SEEK_END)
    fh.write("\n];")
    fh.close()
        
