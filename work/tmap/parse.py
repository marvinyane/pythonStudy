#! /usr/bin/python

import sys, os

f = open('include/pset_bt_general_if.h')
fw = open('result.h', 'w')

names = filter(lambda x : x.find('uint8') == 0, f)

names = map(lambda x : x.replace(';', ''), names)

for name in names:
    funcName = name.split('(')[0].split()[1]
    params = name.split('(')[1].replace(')','').split(',')

    fw.write(name)
    fw.write('{\n')
    fw.write("%s(" % funcName.replace('BtApp', 'BtGen'))

    for i, p in enumerate(params):
        if p.find('void') == -1:
            fw.write("%s" % p.split()[1].replace('*', ''))
            if i < len(params) - 1:
                fw.write(", ")

    fw.write(");\n}\n")

f.close()
fw.close()


