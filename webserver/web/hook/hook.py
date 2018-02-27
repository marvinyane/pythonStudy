#! /usr/bin/env python

import web

def my_processor(handler):
    print 'before handling'
    result = handler()
    print 'after handling'
    return result

def my_loadhook():
    print "my load hook"

def my_unloadhook():
    print "my unload hook"

urls = ("/.*", "example")

app = web.application(urls, globals())
app.add_processor(web.loadhook(my_loadhook))
app.add_processor(web.unloadhook(my_unloadhook))

class example:
    def GET(self):
        return "hello"

if __name__ == '__main__':
    app.run()
