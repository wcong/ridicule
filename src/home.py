# encoding=utf8
__author__ = 'wcong'

import web

import util

import config


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        email = util.get_user_email()
        user_id = util.get_user_id_by_email(email)
        user_id_list = Index.get_readable_user_id(user_id)
        ridicule_list = Index.get_ridicule_by_user_id(user_id_list)
        data = dict()
        data['ridicule_list'] = ridicule_list
        return config.render.home(data)

    @staticmethod
    def get_ridicule_by_user_id(user_id_list):
        sql = 'select id,user_id,content from db_ridicule where user_id in (' + ','.join(
            user_id_list) + ') order by create_time desc'
        data = list(config.mysql.query(sql))
        return data

    @staticmethod
    def get_readable_user_id(user_id):
        sql = 'select related_user_id from db_relationship where main_user_id=' + str(user_id) + ' and is_readable =1'
        data = list(config.mysql.query(sql))
        user_id_list = list()
        user_id_list.append(str(user_id))
        for i in data:
            user_id_list.append(str(i['related_user_id']))
        return user_id_list


app_home = web.application(urls, locals())