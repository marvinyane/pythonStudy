#! /usr/bin/env python

import web

urls = ("/", "index")

app = web.application(urls, globals())

class index:
    def GET(self):
        c = web.cookies().get('age')
        if c is None:
            web.setcookie('age', 25, 3600)
            return "Age set in your cookie is 25"
        else:
            return "Your age is :" + c

if  __name__ == '__main__':
    app.run()
