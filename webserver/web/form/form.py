#! /usr/bin/env python

import web
from web import form

render = web.template.render('templates/')

vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
vemail = form.regexp(r".*@.*", 'must be a valid email address')

register_form = form.Form(
        form.Textbox("username", description="Username"),
        form.Textbox("email", vemail, description="E-Mail"),
        form.Password("password", vpass, description="Password"),
        form.Password("password2", description="Repeat password"),
        form.Button("submit", type="submit", description="Register"),
        validators=[form.Validator("Passwords did't match", lambda i : i.password == i.password2)]
    )

urls = ("/", "register")
app = web.application(urls, globals())

class register:
    def GET(self):
        f = register_form()
        return render.register(f)
    def POST(self):
        f = register_form()
        if not f.validates():
            return render.register(f)
        else:
            return f.password


if __name__ == '__main__':
    app.run()
