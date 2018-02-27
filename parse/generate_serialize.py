#!/usr/bin/python

import os
import sys
import string
import parse_xml

from generate_headers_header import *
from generate_types import *

def create_serialize(cmds, tag):
    filename = 'stc_%s_serialize.c' % (tag)
    fh = open(filename, "w")

    create_file_note(fh, filename)
    fh.write('#include "stc_serialize_utils.h"\n')
    fh.write('#include "stc_%s_cpuif_opcode.h"\n' % (tag))
    fh.write('#include "stc_%s_cpuif_cmd.h"\n' % (tag))

    # Serialize Get Len
    fh.write('static uint16 serialize_%s_get_len(uint16 opcode, void *data)\n' % (tag))
    fh.write('{\n\tuint16 length = 0;\n\tswitch(opcode)\n\t{\n')
    for cmd in cmds:
        if(len(cmd['params']) != 0):
            fh.write('\tcase %s:\n\t{\n' % cmd['name'])
            fh.write('\t\t%s_T *prim = data;\n' % cmd['name'])
            for param in cmd['params']:
                if(param['type'] == 'buff') or (param['type'] == 'str'):
                    # Buffer or string
                    fh.write('\t\tlength += prim->%sLen;\t/* %s */\n' % (param['name'], param['name']))
                else:
                    # Check array
                    m = check_array(param['name'])
                    if m:
                        fh.write('\t\tlength += %s;\t\t\t/* %s */\n' % (m.group(2), param['name']))
                    else:
                        param_len = type_len[param['type']]
                        fh.write('\t\tlength += %d;\t\t\t/* %s */\n' % (param_len, param['name']))
            fh.write('\t\tbreak;\n\t}\n')
    fh.write('\tdefault:\n\t\tbreak;\n\t}\n')
    fh.write('\n\treturn length;\n}\n')

    # Serialize
    fh.write('''
uint8* stc_%s_serialize(uint16 opcode, void *msg, uint16 *length)
{
    uint16 msgLen = serialize_%s_get_len(opcode, msg);
    uint8 *buf = NULL;
    uint8 *p = NULL;

    *length = msgLen + OPCODE_HEADER_LEN + OPCODE_MSG_TYPE;
    p = buf = StcMemAlloc(*length);
    if(NULL == buf)
        return NULL;

    SET_UINT16(opcode);
    SET_UINT16(*length);

    if (*length > 128) 
    {
        SET_UINT16(1);
    }
    else
    {
        SET_UINT16(0);
    }

    switch(opcode)
    {
''' % (tag, tag))

    for cmd in cmds:
        if(len(cmd['params']) != 0):
            fh.write('\tcase %s:\n\t{\n' % cmd['name'])
            fh.write('\t\t%s_T *prim = msg;\n' % cmd['name'])
            for param in cmd['params']:
                if (param['type'] == 'buff') or (param['type'] == 'str'):
                    # Buffer or string
                    fh.write('\t\tSET_BUFFER(prim->%s, prim->%sLen);\n' % (param['name'], param['name']))
                else:
                    # Check array
                    m = check_array(param['name'])
                    if m:
                        fh.write('\t\tSET_BUFFER(prim->%s, %s);\n' % (m.group(1), m.group(2)))
                    else:
                        fh.write('\t\tSET_%s(prim->%s);\n' % (types[param['type']].upper(), param['name']))
            fh.write('\t\tbreak;\n\t}\n')
    fh.write('\tdefualt:\n\t\tbreak;\n\t}\n\n')
    fh.write('\n\treturn buf;\n}')

    fh.close()


if __name__ == '__main__':
    file = sys.argv[1]
    tag = sys.argv[2]
    if not os.path.exists(file):
        sys.exit(1)

    cmds = parse_xml.load_xml_file(file)

    create_serialize(cmds, tag)
