#! /usr/bin/python

import web
import time

urls = ("/.*", "hello",
        "/(.*)/", "redirect")

app = web.application(urls, globals())

class hello:
    def GET(self):
        time.sleep(100)
        return "Hello world!"

class redirect:
    def GET(self, path):
        print "redirect!"
        return web.seeother("/"+path)

if __name__ == "__main__":
    app.run()
