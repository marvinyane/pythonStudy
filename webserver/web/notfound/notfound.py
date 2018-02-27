#! /usr/bin/env python

import web

urls = ("/", "index")

app = web.application(urls, globals())

def notfound():
    return web.notfound("sorry, not found")

app.notfound = notfound

def internalerror():
    return web.internalerror("Bad, bad server")

app.internalerror = internalerror

class index:
    def GET():
        raise web.notfound()


if __name__ == '__main__':
    app.run()
