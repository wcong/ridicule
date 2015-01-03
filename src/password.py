# encoding=utf8
__author__ = 'wcong'

import web
import util
import config
import pdbc


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        user = pdbc.User.select_all_by_id(user_id)
        data = dict()
        data['user'] = user
        return config.render.password(data)

    def POST(self):
        email = util.get_user_email()
        password = web.input().get("password")
        repeat_password = web.input().get("repeat_password")
        if password != repeat_password:
            web.seeother('./')
            return
        pdbc.User.update_password_by_email(email, password)
        web.seeother('../home/')


app_password = web.application(urls, locals())