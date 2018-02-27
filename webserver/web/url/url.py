#! /usr/bin/python

import web

urls = ("/tasks/list/(.+)", "list_users")
app = web.application(urls, globals())

class list_users:
    def GET(self, name):
        return "task to list users {0}".format(name)

if __name__ == '__main__':
    app.run()
