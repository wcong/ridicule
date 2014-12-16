# encoding=utf8
__author__ = 'wcong'

import config
import web
import util
import pdbc

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        email = util.get_user_email()
        user_id = util.get_user_id_by_email(email)
        user = pdbc.User.select_all_by_id(user_id)
        data = dict()
        data['user'] = user
        return config.render.nickname(data)

    def POST(self):
        email = util.get_user_email()
        user_id = util.get_user_id_by_email(email)
        nickname = web.input().get("nickname")
        is_nickname = web.input().get("is_nickname")
        if is_nickname == 'on':
            is_nickname = 1
        else:
            is_nickname = 0
        set_list = list()
        set_list.append('nickname="' + nickname + '"')
        set_list.append('is_nickname=' + str(is_nickname))
        pdbc.User.update_list_by_id(user_id, set_list)
        web.seeother('../home/')


app_nickname = web.application(urls, locals())