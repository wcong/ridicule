# encoding=utf8
__author__ = 'wcong'

import web
import util
import config
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
            return config.render.home()

    def get_json(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        user_id_list = Index.get_readable_user_id(user_id)
        ridicule_list = pdbc.Ridicule.get_ridicule_by_user_id_list(user_id_list)
        user_map = pdbc.User.get_user_map_by_user_id(user_id_list)
        data = dict()
        data['ridicule_list'] = ridicule_list
        data['user_map'] = user_map
        return json.dumps(data)

    @staticmethod
    def get_readable_user_id(user_id):
        data = pdbc.Friend.select_open_friends_by_user_id(user_id)
        user_id_list = list()
        user_id_list.append(str(user_id))
        for i in data:
            user_id_list.append(str(i['related_user_id']))
        return user_id_list


app_home = web.application(urls, locals())