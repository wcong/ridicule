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
        user_id_list = Index.get_readable_user_id(user_id)
        ridicule_list = pdbc.Ridicule.get_ridicule_by_user_id_list(user_id_list)
        data = dict()
        data['ridicule_list'] = ridicule_list
        return config.render.home(data)


    @staticmethod
    def get_readable_user_id(user_id):
        data = pdbc.Friend.select_open_friends_by_user_id(user_id)
        user_id_list = list()
        user_id_list.append(str(user_id))
        for i in data:
            user_id_list.append(str(i['related_user_id']))
        return user_id_list


app_home = web.application(urls, locals())