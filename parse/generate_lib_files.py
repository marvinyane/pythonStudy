#!/usr/bin/python

import os
import sys
import string
import parse_xml

from generate_headers_header import *
from generate_types import *

def get_string_lines(note, size):
    notes = []

    while len(note) > size:
        line = note[:size]
        if note[size-1] != ' ' and note[size] != ' ':
            line = line + '-'
        notes.append(line)
        note = note[size:]
    else:
        notes.append(note)

    return notes


def create_func_note(fh, cmd):
    func_note = cmd['function']
    func_note = " ".join(func_note.split("\n"))

    func_notes = get_string_lines(func_note, 80)

    fh.write("\n/*!\n")
    fh.write("\t@brief:\n")
    for func_note in func_notes:
        fh.write("\t\t%s\n" %(func_note))

    for param in cmd['params']:
        fh.write("\t@param: %s\n" % param['name'])
        param_note = param['meaning'].strip()
        param_notes = []
        if param_note != None or len(param_note) > 0:
            param_note = " ".join(param_note.split("\n"))
            param_notes = get_string_lines(param_note, 80)

        for note in param_notes:
            fh.write("\t\t%s\n" % note)
    fh.write("\n*/\n")


def special_func_imple(tag, fh):
    if tag == 'BT_GEN_POWER_ON_REQ':
        fh.write('\tif (BtPowerOnReq(&addr))\n')
        fh.write('\t{\n\t\treturn CMD_OK;\n\t}\n')
        fh.write('\treturn CMD_ERROR;\n')
        return False
    elif tag == 'BT_GEN_POWER_OFF_REQ':
        fh.write('\tBtPowerOffReq();\n\treturn CMD_OK;\n')
        return False
    elif tag == 'BT_GEN_GET_LOCAL_VERSION_REQ':
        fh.write('\tif(versionlen != BLUETEC_VERSION_LEN)\n\t\treturn CMD_ERROR;\n\n')
        fh.write('\tversion[0] = (BLUETEC_VERSION >> 8) & 0xFF;\n\tversion[1] = BLUETEC_VERSION & 0xFF;\n')
        fh.write('\treturn CMD_OK;\n');
        return False
    else:
        return True

def create_hif(cmds, tag):
    filename = 'stc_%s_cpuif_opcode.h' % tag
    fh = open(filename, 'w')
    generate_headers_header(fh, filename)

    fh.write('#include "stc_sched_types.h"\n')
    for cmd in cmds:
        name = "{:<50}".format(cmd['name'])
        fh.write("#define %s (0x%04x)\n" %(name, int(cmd['opcode'], 16)))
    
    # Struct
    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag:
            create_func_note(fh, cmd)
            f_name = '%s_T' % cmd['name']
            fh.write('typedef struct{\n')
            for param in cmd['params']:
                fh.write("\t%s %s;\n" %(types[param['type']], param['name']))
            fh.write("} %s;\n\n" %(f_name))

    generate_headers_tail(fh)
    fh.close()

def create_header(cmds, tag):
    filename = 'stc_%s_cpuif_cmd.h' % tag
    fh = open(filename, 'w')

    create_file_note(fh, filename)
    generate_headers_header(fh, filename)

    fh.write('#include "stc_sched_types.h"\n')

    # Function Call
    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag:
            create_func_note(fh, cmd)
            func_name = create_func(cmd['name'], cmd['params'], 'uint8')
            fh.write("%s;\n" %(func_name))

    generate_headers_tail(fh)
    fh.close()

def create_source(cmds, tag):
    filename = 'stc_%s_cpuif_cmd.c' % tag
    fh = open(filename, 'w')

    create_file_note(fh, filename)

    fh.write('#include "stc_%s_cpuif_opcode.h"\n' % tag)
    fh.write('#include "stc_%s_cpuif_cmd.h"\n' % tag)
    fh.write('#include "stc_serialize_utils.h"\n\n')
    fh.write('extern uint8* stc_%s_serialize(uint16 opcode, void* msg, uint16* length);\n\n' % (tag))

    for cmd in cmds:
        l = cmd['name'].lower().split('_')
        if l[1] == tag:
            func_name = create_func(cmd['name'], cmd['params'], 'uint8')
            fh.write("%s\n{\n" % (func_name))

            if special_func_imple(cmd['name'], fh):
                fh.write('\tuint16 _len = 0;\n')
                fh.write('\tuint8* _data = NULL;\n')
                fh.write('\tMAKE_MESSAGE(%s);\n' %cmd['name'])
                for param in cmd['params']:
                    if param['type'] == 'buff':
                        name = param['name']
                        fh.write('\tif(%sLen){\n\t\tif(%s){\n' % (name, name))
                        fh.write('\t\t\tmsg->%s = malloc(%sLen);\n' % (name, name))
                        fh.write('\t\t\tif(msg->%s)\n' % name)
                        fh.write('\t\t\t\tmemcpy(msg->%s, %s, %sLen);\n' % (name, name, name))
                        fh.write('\t\t\telse\n\t\t\t\treturn CMD_ERROR;\n')
                        fh.write('\t\t}\n\t\telse\n\t\t\treturn CMD_ERROR;\n\t}\n')
                    elif param['type'] == 'str':
                        name = param['name']
                        fh.write('\tif(%sLen){\n\t\tif(%s){\n' % (name, name))
                        fh.write('\t\t\tmsg->%s = malloc(%sLen + 1);\n' % (name, name))
                        fh.write('\t\t\tif(msg->%s)\n' % name)
                        fh.write('\t\t\t\tmemcpy(msg->%s, %s, %sLen);\n' % (name, name, name))
                        fh.write('\t\t\telse\n\t\t\t\treturn CMD_ERROR;\n')
                        fh.write('\t\t}\n\t\telse\n\t\t\treturn CMD_ERROR;\n\t}\n')
                    else:
                        # Check array
                        m = check_array(param['name'])
                        if m:
                            fh.write('\tmemcpy(msg->%s, %s, %s);\n' % (m.group(1), m.group(1), m.group(2)))
                        else:
                            fh.write('\tmsg->%s = %s;\n' %(param['name'], param['name']))

                fh.write('\t_data = stc_%s_serialize(%s, msg, &_len);\n' % (tag, cmd['name']))
                fh.write('\treturn SendMessageToRemote(_data, _len);\n')
            fh.write('}\n\n')
    fh.close()

if __name__ == '__main__':
    file = sys.argv[1]
    tag = sys.argv[2]
    if not os.path.exists(file):
        sys.exit(1)

    cmds = parse_xml.load_xml_file(file)

    filename = ''.join(file.split('.')[:-1]).lower()

    print filename

    # open status file, define the structure.

    create_hif(cmds, tag)
    create_header(cmds, tag)
    create_source(cmds, tag)

