#!/usr/bin/env python
# encoding=utf8

import sys
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
    '/register', register.app_register,
    '/ridicule', ridicule.app_ridicule
)

web.config.debug = True


def login_hook(handle):
    if web.ctx.get("path") in ['/login/', '/register/', '/invite/']:
        return handle()
    log_user = web.cookies().get("email")
    last_visit_time = web.cookies().get("last_visit_time")
    if log_user is None or last_visit_time is None:
        raise web.seeother("/invite/")
    last_visit_time = util.decode_string(last_visit_time)
    last_visit_time = int(last_visit_time)
    now = util.make_time_stamp()
    time_interval = now - last_visit_time
    if time_interval > config.log_time_interval:
        raise web.seeother("/invite/")
    return handle()


class Index:
    def GET(self):
        return config.render.index()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.add_processor(login_hook)
    app.run()

