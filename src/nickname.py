# encoding=utf8
__author__ = 'wcong'

import config
import web
import util
import pdbc
import json

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        if util.is_json_request():
            return self.get_json()
        else:
            return config.render.nickname()

    def get_json(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        user = pdbc.User.select_all_by_id(user_id)
        data = dict()
        data['user'] = user
        return json.dumps(data)

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        nickname = web.input().get("nickname")
        is_nickname = web.input().get("is_nickname")
        set_list = list()
        set_list.append('nickname="' + nickname + '"')
        set_list.append('is_nickname=' + str(is_nickname))
        pdbc.User.update_list_by_id(user_id, set_list)
        web.seeother('../home/')


app_nickname = web.application(urls, locals())