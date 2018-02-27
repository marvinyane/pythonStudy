#! /usr/bin/python3

d = {}
d['className'] = 'MyCPlusPlusClassName'
d['classType'] = 'MyCPlusPlusClassType'

print("{className} - {classType}".format(**d))

#with open('t', 'r') as ftemp:
#    templateString = ftemp.read()
#with open('tt', 'w') as f:
#    f.write(templateString.format(**d))
