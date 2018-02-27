#! /usr/bin/env python

import web
from web import form

render = web.template.render('templates/')

vid = form.regexp(r"\d{4}$", 'must be 4 numbers')

register_form = form.Form(
        form.Textbox("name", description="Name"),
        form.Password("id", vid, description="Number"),
        form.Button("submit", type="submit", description="Register")
    )

urls = ("/", "register")
app = web.application(urls, globals())

class register:
    def GET(self):
        f = register_form()
        return render.register(f)
    def POST(self):
        f = register_form()
        return f.name


if __name__ == '__main__':
    app.run()
