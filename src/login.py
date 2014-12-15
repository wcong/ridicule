# encoding=utf8
__author__ = 'wcong'

import web

import util

import config


urls = (
    '/', 'Index'
)


class Index():
    def GET(self):
        return config.render.login()

    def POST(self):
        email = web.input().get("email")
        password = web.input().get("password")
        sql = 'select count(*) from db_user where email ="' + email + '" and password="' + util.encode_string(
            password) + '"'
        result = list(config.mysql.query(sql))
        if len(result) > 0:
            web.setcookie("email", util.decode_string(email))
        web.seeother('/home')


app_login = web.application(urls, locals())