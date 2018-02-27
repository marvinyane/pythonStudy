#! /usr/bin/env python

import web

urls = ("/post", "postHandler")

app = web.application(urls, globals())

class postHandler:
    def GET(self):
        return "Hello, please post"

    def POST(self):
        data = web.data()
        print data

if __name__ == '__main__':
    app.run()
