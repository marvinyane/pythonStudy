#! /usr/bin/python

import requests

url = 'http://www.zhihu.com/login'

payload = {'email' : 'fcyjzh1216@163.com', 'password':'123456', 'rememberme':'n'}

r = requests.post(url, data=payload)

fh = open('a.html', 'w')

fh.write(r.content)

fh.close()
