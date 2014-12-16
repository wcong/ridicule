# encoding=utf8
__author__ = 'wcong'

import web
import config
import util
import pdbc

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        email = util.get_user_email()
        user_id = util.get_user_id_by_email(email)
        ridicule_list = pdbc.Ridicule.select_by_user_id(user_id)
        data = dict()
        data['list'] = ridicule_list
        return config.render.my(data)


app_my = web.application(urls, locals())