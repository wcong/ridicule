# encoding=utf8
__author__ = 'wcong'

import config
import web
import util
import pdbc

urls = (
    '/', 'Index',
    '/old', 'Old',
    '/find', 'Find'
)


class Index:
    def GET(self):
        return config.render.friends()


class Old:
    def GET(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)

        return config.render.old_friends()


class Find:
    def GET(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        return config.render.find_friends()


app_friends = web.application(urls, locals())