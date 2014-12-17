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
        return config.render.setting(data)


app_setting = web.application(urls, locals())