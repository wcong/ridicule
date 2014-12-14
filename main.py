#!/usr/bin/env python
# encoding=utf8

import sys
import base64
import datetime

import web

from src import *


reload(sys)
sys.setdefaultencoding('utf-8')

'''
ok this is our main page
'''

urls = (
    '/', 'Index',
    '/login', login.app_login,
    '/home', home.app_home,
    '/setting', setting.app_setting,
    '/invite', invite.app_invite,
    '/register', register.app_register
)

web.config.debug = True


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
        return config.render.index()


if __name__ == "__main__":
    app = web.application(urls, globals())
    # app.add_processor(login_hook)
    app.run()

