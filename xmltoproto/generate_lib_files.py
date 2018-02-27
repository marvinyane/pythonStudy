#!/usr/bin/python3

import os
import sys
import string
import parse_xml

from generate_headers_header import *

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

names = {
        "gen" : "general",
        "cm"  : "connect",
        "hfp" : "phone",
        "av"  : "audio",
        "pbdl" : "phonebook",
        "spp" : "spp"
        }

def create_func(name, params, rvalue):
    f_name = string.capwords(name, '_')
    f_name = ''.join(f_name.split('_'))
    str = "%s %s(" % (rvalue, f_name)

    start = True
    for param in params:
        if param['type'] in types:
            if start:
                start = False
            else:
                str = "%s, " % str
            str = "%s%s %s" %(str, types[param['type']], param['name'].lower())
        else:
            print('error : unknown %s ' % (param['type']))
    str = "%s)" % str

    return str

def create_hif(cmds):
    fh = open('bluetec_hif.h', 'w')
    generate_headers_header(fh, 'bluetec_hif.h')
    for cmd in cmds:
        name = "{:<50}".format(cmd['name'])
        fh.write("#define %s (0x%04x)\n" %(name, int(cmd['opcode'], 16)))

    generate_headers_tail(fh)
    fh.close()

def create_header(cmds, tag):
    filename = 'bluetec_%s_if.h' % names[tag]
    filename_cmd = 'app_%s_cmd.h' % tag
    filename_evt = 'app_%s_evt.h' % tag
    fh = open(filename, 'w')
    fh_cmd = open(filename_cmd, 'w')
    fh_evt = open(filename_evt, 'w')

    generate_headers_header(fh, filename)
    generate_headers_header(fh_cmd, filename_cmd)
    generate_headers_header(fh_evt, filename_evt)
    
    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag and (l[-1] == 'req' or l[-1] == 'res'):
            func_name = create_func(cmd['name'], cmd['params'], 'uint8')
            fh.write("%s;\n" %(func_name))
            
            req_name = '%s_T' % cmd['name']
            fh_cmd.write('typedef struct{\n')

            for param in cmd['params']:
                fh_cmd.write("\t%s %s;\n" %(types[param['type']], param['name'].lower()))
            fh_cmd.write("} %s;\n\n" %(req_name))

    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag and (l[-1] == 'cfm' or l[-1] == 'ind'):
            func_name = create_func(cmd['name'], cmd['params'], 'void')
            fh_evt.write("%s;\n" %func_name)
            f_name = '%s_T' % cmd['name']
            fh.write('typedef struct{\n')
            for param in cmd['params']:
                if param['type'] in types:
                    fh.write("\t%s %s;\n" %(types[param['type']], param['name'].lower()))
                else:
                    print('error : unknown %s ' % (param['type']))

            fh.write("} %s;\n\n" %(f_name))

    generate_headers_tail(fh)
    generate_headers_tail(fh_cmd)
    generate_headers_tail(fh_evt)

    fh.close()
    fh_cmd.close()
    fh_evt.close()

def create_source(cmds, tag):
    filename = 'app_%s_cmd.c' % tag
    fh = open(filename, 'w')
    
    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag and (l[-1] == 'req' or l[-1] == 'res'):
            func_name = create_func(cmd['name'], cmd['params'], 'uint8')
            fh.write("%s\n{\n" % (func_name))

            fh.write('\tMAKE_MESSAGE_AFTER_POWERON(%s);\n' %cmd['name'])
            for param in cmd['params']:
                if types[param['type']] == 'uint8*':
                    fh.write('\tmsg->%s = BtPmemZalloc(%sLen/*TODO*/);\n' %(param['name'].lower(), param['name'].lower()))
                    fh.write('\tBtMemCpy(msg->%s, %s, %sLen/*TODO*/);\n' %(param['name'].lower(), param['name'].lower(),
                        param['name'].lower()))
                else:
                    fh.write('\tmsg->%s = %s;\n' %(param['name'].lower(), param['name'].lower()))

            fh.write('\treturn SendMessage(get%sCmdHandle(), %s, msg);\n' %(tag.capitalize(), cmd['name']))
            fh.write('}\n\n')
    fh.close()

    filename = 'app_%s_evt.c' % tag
    fh = open(filename, 'w')

    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag and (l[-1] == 'cfm' or l[-1] == 'ind'):
            f_name = string.capwords(cmd['name'], '_')
            f_name = ''.join(f_name.split('_'))
            fh.write("void %s(" % (f_name))

            start = True
            for param in cmd['params']:
                if param['type'] in types:
                    if start:
                        start = False
                    else:
                        fh.write(', ')
                    fh.write("%s %s" %(types[param['type']], param['name'].lower()))
                else:
                    print('error : unknown %s ' % (param['type']))
            fh.write(")\n")
            fh.write('{\n')
            fh.write('\tMAKE_EVENT(%s);\n' %cmd['name'])
            for param in cmd['params']:
                fh.write('\tmsg.%s = %s;\n' %(param['name'].lower(), param['name'].lower()))

            fh.write('\tbtSend%sMsg(%s, &msg);\n' %(tag.capitalize(), cmd['name']))
            fh.write('}\n\n')
    fh.close()

if __name__ == '__main__':
    file = sys.argv[1]
    if not os.path.exists(file):
        sys.exit(1)
    
    cmds = parse_xml.load_xml_file(file)

    filename = ''.join(file.split('.')[:-1]).lower()
    
    # open status file, define the structure.
    create_hif(cmds)

    for tag in names:
        create_header(cmds, tag)
        create_source(cmds, tag)

