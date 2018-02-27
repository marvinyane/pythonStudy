#! /usr/bin/python

import httplib,urllib

params = urllib.urlencode({"question_2755" : "10493"})

headers = {"Origin":"http://cgi.mmog.163.com:8088",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept":"application/json, text/javascript, */*",
    "Referer":"http://cgi.mmog.163.com:8088/v4a/show_vote/1106/?6",
    "X-Requested-With":"XMLHttpRequest",
    "Connection":"keep-alive"}


conn = httplib.HTTPConnection("cgi.mmog.163.com:8088")

conn.request("POST", "/v4a/show_vote/1106/", params, headers)

response = conn.getresponse()

print(response.status, response.reason)

data = response.read()
fh = open('rece.html', 'w')
fh.write(data)
fh.close()

conn.close()
