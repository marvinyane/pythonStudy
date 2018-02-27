#! /usr/bin/env python
import web

urls = ("/.*", "example")

app = web.application(urls, globals())

class example:
    def GET(self):
        refer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
        ip = web.ctx.ip
        print ip
        raise web.seeother(refer)



if __name__ == '__main__':
    app.run()
