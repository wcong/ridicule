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
        friend_list = pdbc.Friend.select_by_user_id(user_id)
        data = dict()
        data['friend_list'] = friend_list
        return config.render.old_friends(data)

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        is_open = web.input().get("is_open")
        friend_id = web.input().get("id")
        if is_open == 'on':
            is_open = 1
        else:
            is_open = 0
        pdbc.Friend.update_is_open(friend_id, is_open)


class Find:
    def GET(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        user = pdbc.User.select_all_by_id(user_id)
        friend_id_list = pdbc.Friend.select_user_id_by_user_id(user_id)
        user_id_list = list()
        for friend in friend_id_list:
            user_id_list.append(str(friend['related_user_id']))
        find_list = pdbc.User.select_by_company_id(user['company_id'], user_id_list)
        data = dict()
        data['find_list'] = find_list
        return config.render.find_friends(data)

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        add_user_id = web.input().get("user_id")
        pdbc.Friend.insert(user_id, add_user_id)
        web.seeother('./old')


app_friends = web.application(urls, locals())