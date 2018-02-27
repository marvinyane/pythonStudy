import web
import sqlite3
import json
from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "server.crt"
CherryPyWSGIServer.ssl_private_key = "server.key"

urls = ("/(.*)", "hello")


def storePostData(d):
    conn = sqlite3.connect('server.db')
    for item in d['data']:
        sql = "insert into postdata (imei, tst, acc, gps, gsm) values (\"%s\",\"%s\", \"%s\", \"%s\", \"%s\")" % (item['IMEI'],
                item['TST'], item['ACC'], item['GPS'], item['GSM'])
        c = conn.cursor()
        c.execute(sql)

    conn.commit()
    conn.close()

def storeRecord(get):
    conn = sqlite3.connect('server.db')

    if get:
        sql = "insert into record(type) values (\"GET\")"
    else:
        sql = "insert into record(type) values (\"POST\")"
    print sql

    c = conn.cursor()
    c.execute(sql)

    conn.commit()
    conn.close()


class MyApplication(web.application):
    def run(self, port=5070, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class hello:
    def GET(self, name):
        print name.split('/')[2]
        storeRecord(True)
    def POST(self, name):
        data = web.data()
        t = json.loads(data)
        storePostData(t)
        storeRecord(False)


if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=5070)
