#!/usr/bin/env python
# encoding=utf8

import sys
import base64
import datetime
import json

import web

import config
from src import *


reload(sys)
sys.setdefaultencoding('utf-8')

'''
ok this is our main page
'''

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/home', 'Home',
    '/setting', 'Setting',
    '/invite', 'Invite',
    '/register', 'Register'
)
web.config.debug = True
render = web.template.render('templates/', cache=False, base="layout")


def login_hook(handle):
    log_user = web.cookies().get("login")
    last_visit_time = web.cookies().get("last_visit_time")
    if not log_user or not last_visit_time:
        web.seeother("/login")
    last_visit_time = base64.decode(last_visit_time)
    last_visit_time = int(last_visit_time)
    now = datetime.datetime.now().time()
    time_interval = now - last_visit_time
    if time_interval > config.log_time_interval:
        web.seeother("/login")


class Index:
    def GET(self):
        return render.index()


class Login:
    def GET(self):
        return render.login()


class Register:
    def GET(self):
        input = web.input()
        email = base64.decode(input.get("email"))
        sign = int(base64.decode(input.get("sign")).replace(email, ''))
        now_time = int(datetime.datetime.now().time())
        if (now_time - sign) > config.log_time_interval:
            web.seeother("/invite")
            return

        return render.register()


class Invite:
    def GET(self):
        return render.invite()

    def POST(self):
        input = web.input()
        if 'email' not in input:
            web.seeother('/invite')
        email = input.get("email")
        register_link_meta = util.make_register_link(email)
        register_link = 'http://' + config.host + '/register?email=' + register_link_meta[0] + '&sign=' + \
                        register_link_meta[1]
        message = '<h1>click the follow links</h2><p>' + register_link + '</p>'
        web.sendmail('redicule@163.com', email, 'register', message)
        result = dict()
        result['success'] = True
        return json.dump(result)


if __name__ == "__main__":
    app = web.application(urls, globals())
    # app.add_processor(login_hook)
    app.run()

