#! /usr/bin/env python
import web

urls = ("/", "index")

app = web.application(urls, globals())

class index:
    def GET(self):
        user_data = web.input()
        return "<h1>" + user_data.id + "</h1>"


if __name__ == '__main__':
    app.run()
