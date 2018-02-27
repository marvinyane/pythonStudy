#! /usr/bin/python
import string
import re

types = {
        "uint8"  : "uint8",
        "uint16" : "uint16",
        "uint32" : "uint32",
        "uint64" : "uint64",
        "int8"   : "int8",
        "int16"  : "int16",
        "int32"  : "int32",
        "int64"  : "int64",
        "bool"   : "uint8",
        "uint8*" : "uint8*",
        "str"    : "uint8*",
        "buff"   : "uint8*",
        }

type_len = {
        "uint8"  : 1,
        "uint16" : 2,
        "uint32" : 4,
        "uint64" : 8,
        "int8"   : 1,
        "int16"  : 2,
        "int32"  : 4,
        "int64"  : 8,
        "bool"   : 1,
        "uint8*" : 0,
        "str"    : 0,
        "buff"   : 0,
        }

names = {
        "wfd" : "wfd",
        }

# tag, [next opcode, last request opcode]
opcodes = {
        "wfd":[1, 1],
        }

def create_opcode(name):
    l = name.lower().split('_')
    tag = l[1]
    code = 0xFFFF
    if tag in opcodes:
        if l[-1] == 'req':
            code = opcodes[tag][0]
            opcodes[tag][0] += 1
            opcodes[tag][1] = code
        elif l[-1] == 'cfm':
            code = opcodes[tag][1] | 0x8000
        elif l[-1] == 'ind':
            code = opcodes[tag][0] | 0x8000
            opcodes[tag][0] += 1
        else:
            print 'Unknown name: %s' + name
    else:
        print 'Unknown tag: %s' + tag
    return '%X' % code


def create_file_note(fh, name):
    fh.write('/**\n')
    fh.write('* Copyright @ 2014 - 2015 Suntec Software(Shanghai) Co., Ltd.\n')
    fh.write('* All Rights Reserved.\n')
    fh.write('*\n')
    fh.write('* Redistribution and use in source and binary forms, with or without\n')
    fh.write('* modification, are NOT permitted except as agreed by\n')
    fh.write('* Suntec Software(Shanghai) Co., Ltd.\n')
    fh.write('*\n')
    fh.write('* Unless required by applicable law or agreed to in writing, software\n')
    fh.write('* distributed under the License is distributed on an "AS IS" BASIS,\n')
    fh.write('* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n')
    fh.write('*/\n\n')

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
            str = "%s%s %s" %(str, types[param['type']], param['name'])
        else:
            print('error : unknown %s ' % (param['type']))
    str = "%s)" % str
    return str

def create_func_without_type(name, params):
    f_name = string.capwords(name, '_')
    f_name = ''.join(f_name.split('_'))
    str = '%s(' % f_name

    start = True
    for param in params:
        if param['type'] in types:
            if start:
                start = False
            else:
                str = '%s, ' % str
            str = '%s%s' % (str, param['name'])
        else:
            print('error: unknow %s' % param['type'])
    str = '%s)' % str
    return str

def check_array(types):
    m = re.match(r'^([\w\d_]+)\[(\d+)\]$', types)
    return m

if __name__ == "__main__":
    print types
