import os
import sys
import pprint
import xml.etree.ElementTree as ET

def parse_param(l):
    cmd_param = {}
    
    cmd_param['name'] = l[0].find('Name').text

    param_type = l[0].find('Type').text

    if(param_type == None or cmd_param['name'] == None):
        return None

    cmd_param['type'] = param_type.lower()

    return cmd_param

def load_xml_file(fileName):
    root = ET.parse(fileName).getroot()
    cmdlist = root.find('CmdList')

    all_items = cmdlist.findall('CMD')
    cmds = []
    for item in all_items:
        cmd = {}
        cmd['name'] = item.find('Name').text
        cmd['opcode'] = item.find('OPCode').text
        
        cmd_params = []

        params = item.findall('Param')

        count = 0
        while count < len(params):
            h = parse_param(params[count:])
            if(h != None):
                cmd_params.append(h)
            count += 1

        cmd['params'] = cmd_params
        cmds.append(cmd)


    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(cmds)
    return cmds

