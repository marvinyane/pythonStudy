#!/usr/bin/python

import os
import sys
import string
import parse_xml

from generate_headers_header import *
from generate_types import *

def create_unserialize(cmds, tag):
    filename = 'stc_%s_unserialize.c' % (tag)
    fh = open(filename, "w")

    create_file_note(fh, filename)
    fh.write('#include "stc_serialize_utils.h"\n')
    fh.write('#include "stc_%s_cpuif_opcode.h"\n' % (tag))
    fh.write('#include "stc_%s_cpuif_cmd.h"\n' % (tag))

    # Serialize
    fh.write('''
uint8 *stc_%s_unserialize(void *data, uint16 dataLen)
{
    uint16 opcode = 0;
    uint8 *p = data;
    uint16 length = 0x00;
    uint16 msg_type = 0x00;
    void *message = NULL;

    opcode = GET_UINT16();
    length = GET_UINT16();
    msg_type = GET_UINT16();
    switch(opcode)
    {
''' % (tag))

    for cmd in cmds:
        if(len(cmd['params']) != 0):
            fh.write('\tcase %s:\n\t{\n' % cmd['name'])
            fh.write('\t\tMAKE_MESSAGE(%s);\n' % cmd['name'])
            for param in cmd['params']:
                if(param['type'] == 'buff') or (param['type'] == 'str'):
                    # Buffer or string
                    fh.write('\t\tmsg->%s = GET_BUFFER(msg->%sLen);\n' % (param['name'], param['name']))
                else:
                    # Check array
                    m = check_array(param['name'])
                    if m:
                        fh.write('\t\tGET_ARRAY(msg->%s, %s);\n' % (m.group(1), m.group(2)))
                    else:
                        fh.write('\t\tmsg->%s = GET_%s();\n' % (param['name'], types[param['type']].upper()))
            fh.write('\t\tmessage = msg;\n');
            fh.write('\t\tbreak;\n\t}\n')
    fh.write('\tdefualt:\n\t\tbreak;\n\t}\n\n')
    fh.write('\n\n\treturn message;\n}')

    fh.close()


if __name__ == '__main__':
    file = sys.argv[1]
    tag = sys.argv[2]
    if not os.path.exists(file):
        sys.exit(1)

    cmds = parse_xml.load_xml_file(file)

    create_unserialize(cmds, tag)
