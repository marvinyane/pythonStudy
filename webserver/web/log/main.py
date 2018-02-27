#! /usr/bin/env python

import web
import mylog

urls = ("/", "index")
app = web.application(urls, globals())

class index:
    def GET(self):
        return "hello"

if __name__ == '__main__':
    app.run(mylog.Log)
