# encoding=utf8
__author__ = 'wcong'

import datetime

import web

import config
import util
import pdbc


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        input = web.input()
        email = util.decode_string(input.get("email"))
        sign = int(util.decode_string(input.get("sign")).replace(email, ''))
        now_time = util.make_time_stamp()
        web.setcookie("email", util.encode_string(email))
        if (now_time - sign) > config.log_time_interval or not pdbc.User.is_check_sign_same(email, input.get("sign")):
            web.seeother("../invite/")
            return
        data = dict()
        data['email'] = email
        return config.render.register(data)

    def POST(self):
        email = util.get_user_email()
        send_email = util.decode_string(web.input().get("email"))
        password = web.input().get("password")
        repeat_password = web.input().get("repeat_password")
        if email != send_email or password != repeat_password:
            web.seeother('../invite/')
            return
        sql = 'update db_user set password="' + util.encode_string(password) + '" where email ="' + email + '"'
        config.mysql.query(sql)
        web.seeother('../login/')


app_register = web.application(urls, locals())