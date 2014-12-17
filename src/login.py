# encoding=utf8
__author__ = 'wcong'

import web
import util
import config
import pdbc


urls = (
    '/', 'Index'
)


class Index():
    def GET(self):
        return config.render.login()

    def POST(self):
        email = web.input().get("email")
        password = web.input().get("password")
        result = pdbc.User.select_login_user(email, password)
        if result > 0:
            web.setcookie("email", util.encode_string(email), path='/')
            web.setcookie("last_visit_time", util.encode_string(str(util.make_time_stamp())), path='/')
        web.seeother('../home/')


app_login = web.application(urls, locals())
