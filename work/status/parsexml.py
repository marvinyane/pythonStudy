#!/usr/bin/python3

import os
import sys
#import pprint
import xml.etree.ElementTree as ET

general_struct_name = ('GEN', 'CM', 'AVP', 'HFP')

general_param_type = ("void", "uint8", "uint16", "uint24", "uint32", "bool", "bdaddr",
                            "int8", "int16", "int24", "int32", "struct")

def param_type_check(t):
    t = t.strip()
    
    if t.lower() == 'list':
        return (0, "{0: <20}".format('struct list_head'))

    if t.lower() in general_param_type:
        return (0, "{0: <20}".format(t.lower()))
    
    value = 1
    param = ""
    
    if t[-1] != '*':
        value = 1
        param = t+'_T'
    elif t[:-1].strip().lower() not in general_param_type:
        value = 1
        param = t[:-1].strip() + '_T*'
    else:
        value = 0
        param = t[:-1].strip().lower()+'*'

    l = (len(param) // 20 + 1) * 20
    if l <= 20:
        param = "{0:20}".format(param)

    return (value , param)
    
def get_child_struct(cmd, cmds):
    ret = []
    for param in cmd.get('params'):
        param_type = param.get('type').strip().split('-')[0]

        if param_type_check(param_type)[0] == 1:
            if(param_type[-1] == '*'):
                param_type = param_type[:-1].strip()

            for cmd_p in cmds:
                if param_type == cmd_p.get('name').strip():
                    ret.append(cmd_p)
                    break
            else:
                sys.stderr.write("%s did not find!\n" %(param_type))

    return ret

def get_parent_struct(cmds):
    for cmd in cmds:
        piece = cmd.get('name').strip().split('_')

        if len(piece) == 3 and piece[2] == 'STATUS' and piece[1] in general_struct_name:
            yield (piece[1], cmd)

def parse_param(l):
    cmd_param = {}
    count = 1

    cmd_param['name'] = l[0].find('Name').text
    cmd_param['mean'] = l[0].find('Meaning').text

    param_type = l[0].find('Type').text

    if(param_type == None or cmd_param['name'] == None):
        return (1, None)

    cmd_param['type'] = param_type

    if(param_type.startswith('struct')):
        extra_len = int(param_type.split('-')[1])

        extra_params = []
        for index in range(extra_len):
            currentCount, h = parse_param(l[count:])
            if(h != None):
                extra_params.append(h)
            count += currentCount

        cmd_param['params'] = extra_params

    return (count, cmd_param)

def load_xml_file(fileName):
    root = ET.parse(fileName).getroot()

    all_items = root.findall('Item')
    cmds = []
    for item in all_items:
        cmd = {}
        cmd['name'] = item.find('Name').text
        cmd['func'] = item.find('Function').text

        cmd_params = []

        params = item.findall('Param')

        count = 0
        while count < len(params):
            currentCount, h = parse_param(params[count:])
            if(h != None):
                cmd_params.append(h)
            count += currentCount

        cmd['params'] = cmd_params
        cmds.append(cmd)


    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(cmds)

    return cmds

def print_space(deep):
    for index in range(deep):
        sys.stdout.write("\t")


def print_param(deep, param):
    if param.get('params') != None:
        print_space(deep)
        sys.stdout.write("struct {\n")

        for p in param.get('params'):
            print_param(deep+1, p)

        print_space(deep)

        if(param.get('type').split('-')[0].endswith('*')):
            sys.stdout.write("}*%s;\n" %(param.get('name')))
        else:
            sys.stdout.write("}%s;\n" %(param.get('name')))
    else:
        types = param.get('type').split('-')
        type_after_check = param_type_check(types[0])[1]
        paramMean = param.get('mean');

        if(paramMean == None):
            paramMean = ''

        if len(types) > 1:
            print_space(deep)
            sys.stdout.write("{0} {1}[{2}];\n".format(type_after_check, param.get('name'), types[1]))
        else:
            print_space(deep)
            sys.stdout.write("{0} {1};\n".format(type_after_check, param.get('name')))


def format_print_struct(cmd, header):
    sys.stdout.write('/' + '*' * 50 + '\n')
    func = cmd.get('func').split('\r')
    for f in func:
        sys.stdout.write("\t%s\n" %(f))

    sys.stdout.write('*' * 50 + '/' + '\n')
    sys.stdout.write("typedef struct { \n")
    if header != None:
        print_space(1)
        sys.stdout.write(header + '\n')

    for p in cmd.get('params'):
        print_param(1, p)

    sys.stdout.write("} %s_T;\n\n" %(cmd.get('name')))

def generate_native_struct(cmd, cmds, header):
    for cmd_p in get_child_struct(cmd, cmds):
        generate_native_struct(cmd_p, cmds, None)

    if cmd['print'] != True:
        format_print_struct(cmd, header)

    cmd['print'] = True

def generate_struct(cmds):
    for cmd in cmds:
        cmd['print'] = False

    for name, cmd in get_parent_struct(cmds):
 #       generate_native_struct(cmd, cmds, 'BT_STATUS_STRUCT_HEAD;')
        generate_native_struct(cmd, cmds, None)

    for cmd in cmds:
        if cmd['print'] == False:
            format_print_struct(cmd,None)

def get_cmd_by_name(name, cmds):
    for cmd in cmds:
        if cmd['name'] == name:
            return cmd
    return None

# rubbish code

def get_print_array_str(s):
    l = []
    names = []
    i = 0

    strs = s.split('.')

    for t in strs:
        if t.endswith('[]'):
            names.append("index{0}".format(i))
            l.append( t[:-2] + '[{0}]'.format(names[-1]))
            i = i + 1
        else:
            l.append(t)

    if len(names) > 0:
        name = ','.join(names)+','
    else:
        name = ''

    return name ,  '.'.join(l)

def format_local_array_define(l, entry):
    tag = '_'.join((l[0],l[1], 'STATUS'))
    totalname = '_'.join(l)
    
    p, q = get_print_array_str(entry)

    sys.stdout.write("#define SET_%s_STATUS(%svalue, len) COPY_BT_STATUS(%s, %s, value, len)\n\n" 
            %(totalname, p, tag, q))
    
    if len(p) > 0 and p[-1] == ',':
        pp = p[:-1]
    else:
        pp = p
    sys.stdout.write("#define CLEAR_%s_STATUS(%s) CLEAR_BT_STATUS(%s, %s)\n\n" 
            %(totalname, pp, tag, q))
    
    sys.stdout.write("#define GET_%s_STATUS(%svaluePtr, len) GET_BT_COPY_STATUS(%s, %s, valuePtr, len)\n\n" 
            %(totalname, p, tag, q ))

def format_array_define(l, entry):
    tag = '_'.join((l[0],l[1], 'STATUS'))
    totalname = '_'.join(l)

    p, q = get_print_array_str(entry)

    sys.stdout.write("#define SET_%s_INDEX_STATUS(index,%s value) SET_BT_STATUS(%s, %s[index], value)\n\n" 
            %(totalname, p, tag, q))
    
    if len(p) > 0 and p[-1] == ',':
        pp = ','+p[:-1]
    else:
        pp = p
    sys.stdout.write("#define CLEAR_%s_INDEX_STATUS(index%s) CLEAR_BT_STATUS(%s, %s[index])\n\n" 
            %(totalname, pp, tag, q))

    sys.stdout.write("#define GET_%s_INDEX_STATUS(index,%s valuePtr) GET_BT_VALUE_STATUS(%s,%s[index],valuePtr)\n\n" 
            %(totalname, p, tag, q))

    sys.stdout.write("#define SET_%s_STATUS(%sbuffer, len) COPY_BT_STATUS(%s, %s, buffer, len)\n\n" 
            %(totalname, p, tag, q))
    
    if len(p) > 0 and p[-1] == ',':
        pp = p[:-1]
    else:
        pp = p
    sys.stdout.write("#define CLEAR_%s_STATUS(%s) CLEAR_BT_STATUS(%s, %s)\n\n" 
            %(totalname, pp, tag, q))
    
    sys.stdout.write("#define GET_%s_STATUS(%sbuffer, len) GET_BT_COPY_STATUS(%s, %s, buffer, len)\n\n" 
            %(totalname, p, tag, q ))
    

def format_value_define(l, entry, addr):
    tag = '_'.join((l[0],l[1], 'STATUS'))
    totalname = '_'.join(l)

    p, q = get_print_array_str(entry)

    sys.stdout.write("#define SET_%s_STATUS(%svalue) SET_BT_STATUS(%s, %s, value)\n\n" 
            %(totalname, p, tag, q))

    sys.stdout.write("#define GET_%s_STATUS(%svaluePtr) GET_BT_VALUE_STATUS(%s, %s, valuePtr)\n\n" 
            %(totalname, p, tag, q))

    if addr:
        if len(p) > 0 and p[-1] == ',':
            pp = p[:-1]
        else:
            pp = p
        sys.stdout.write("#define CLEAR_%s_STATUS(%s) CLEAR_BT_STATUS(%s, %s)\n\n" 
            %(totalname, pp, tag, q))


def format_struct_define(l, entry):
    tag = '_'.join((l[0],l[1], 'STATUS'))
    totalname = '_'.join(l)
    
    p, q = get_print_array_str(entry)
    
    sys.stdout.write("#define SET_%s_STATUS(%sbuffer) COPY_BT_STATUS(%s, %s, buffer, sizeof(%s))\n\n" 
            %(totalname, p, tag, q, q))
    
    if len(p) > 0 and p[-1] == ',':
        pp = p[:-1]
    else:
        pp = p
    sys.stdout.write("#define CLEAR_%s_STATUS(%s) CLEAR_BT_STATUS(%s, %s)\n\n" 
            %(totalname, pp, tag, q))
    
    sys.stdout.write("#define GET_%s_STATUS(%sbuffer) GET_BT_COPY_STATUS(%s, %s, buffer, sizeof(%s))\n\n" 
            %(totalname, p, tag, q, q))

# deep is for array
def generate_native_define(l, params, cmds, e):
    for param in params:
        list = l[:]
        entry = e[:]

        piece = param['type'].split('-')
        list.append(param['name'].upper())
        entry += param['name']
        
        if len(piece) > 1 and piece[0].lower() in general_param_type:
            format_local_array_define(list[:], entry)
        elif len(piece) > 1 and piece[0].lower() not in general_param_type:
            format_array_define(list[:], entry)
            cmd = get_cmd_by_name(piece[0], cmds)
            if cmd != None:
                generate_native_define(list[:], cmd['params'], cmds, entry+'[].')
        elif piece[0].lower() == 'bdaddr':
            format_value_define(list[:], entry, True)
        elif piece[0][-1] == '*' or piece[0].lower() in general_param_type:
            format_value_define(list[:], entry, False)
        else:
            cmd = get_cmd_by_name(piece[0], cmds)
            if cmd != None:
                generate_native_define(list[:], cmd['params'], cmds, entry+'.')

            format_struct_define(list[:], entry)

def generate_define(cmds):
    for name, cmd in get_parent_struct(cmds):
        list = ['BT']
        list.append(name.upper())

        generate_native_define(list, cmd['params'], cmds, '')

def generate_file_header(name, type):
    sys.stdout.write("#ifndef __PSET_BT_STATUS_%s_%s_H__\n" %(name.upper(), type.upper()))
    sys.stdout.write("#define __PSET_BT_STATUS_%s_%s_H__\n\n" %(name.upper(), type.upper()))

    sys.stdout.write('#ifdef __cplusplus\n')
    sys.stdout.write('extern "C" {\n')
    sys.stdout.write('#endif\n\n')

    if type == 'define':
        sys.stdout.write('#include "pset_bt_status_init.h"\n')
        sys.stdout.write('#include "pset_bt_%s.h"\n\n' %(name))
    else:
        sys.stdout.write('#include "pset_types.h"\n')


def generate_file_tail():
    sys.stdout.write('\n#ifdef __cplusplus\n')
    sys.stdout.write('}\n')
    sys.stdout.write('#endif\n\n')
    sys.stdout.write('#endif/**/\n')

def usage():
    print('\nMake sure the version of python larger than 3.2\n')
    print('Usage: ./parsexml.py name.xml')
    print('Generated Files: pset_bt_name.h & pset_bt_name_define.h\n')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage()
        assert True

    files = sys.argv[1:]

    for file in files:
        if not os.path.exists(file):
            sys.stderr.write("%s is not exist! \n" %(file))
            continue

        cmds = load_xml_file(file)

        filename = ''.join(file.split('.')[:-1]).lower()
        
        # open status file, define the structure.
        fh = open('pset_bt_'+filename+'.h', 'w')
        sys.stdout = fh

        generate_file_header(filename, 'struct')
        generate_struct(cmds)
        generate_file_tail()

        fh.close()

        # open the defined file, add the macro
        fh = open('pset_bt_'+filename+'_define.h', 'w')
        sys.stdout = fh
        
        generate_file_header(filename, 'define')
        generate_define(cmds)
        generate_file_tail()

        fh.close()

