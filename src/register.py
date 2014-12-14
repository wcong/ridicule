# encoding=utf8
__author__ = 'wcong'

import base64
import datetime

import web

import config


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        input = web.input()
        email = base64.decode(input.get("email"))
        sign = int(base64.decode(input.get("sign")).replace(email, ''))
        now_time = int(datetime.datetime.now().time())
        if (now_time - sign) > config.log_time_interval:
            web.seeother("/invite")
            return

        return config.render.register()


app_register = web.application(urls, locals())