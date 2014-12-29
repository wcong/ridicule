# encoding=utf8
__author__ = 'wcong'

import config
import web
import util
import pdbc
import json

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
        if web.input().get("is_clear_reminder") is not None:
            email = util.get_user_email()
            user_id = pdbc.User.select_id_by_email(email)
            pdbc.ReminderFriend.clear_reminder(user_id)
        if util.is_json_request():
            return self.get_json()
        else:
            return config.render.old_friends()

    def get_json(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        friend_list = pdbc.Friend.select_by_user_id(user_id)
        user_id_list = list()
        for friend in friend_list:
            user_id_list.append(str(friend['related_user_id']))
        user_map = pdbc.User.get_user_map_by_user_id(user_id_list)
        data = dict()
        data['friend_list'] = friend_list
        data['user_map'] = user_map
        return json.dumps(data)

    def POST(self):
        # email = util.get_user_email()
        # user_id = pdbc.User.select_id_by_email(email)
        is_open = web.input().get("is_open")
        friend_id = web.input().get("id")
        if is_open == '1':
            is_open = 1
        else:
            is_open = 0
        pdbc.Friend.update_is_open(friend_id, is_open)


class Find:
    def GET(self):
        if util.is_json_request():
            return self.get_json()
        else:
            return config.render.find_friends()

    def get_json(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        user = pdbc.User.select_all_by_id(user_id)
        friend_id_list = pdbc.Friend.select_main_user_id_by_user_id(user_id)
        user_id_list = list()
        for friend in friend_id_list:
            user_id_list.append(str(friend['main_user_id']))
        user_id_list.append(str(user_id))
        find_list = pdbc.User.select_by_company_id(user['company_id'], user_id_list)
        user_id_list = list()
        for friend in find_list:
            user_id_list.append(str(friend['id']))
        user_map = pdbc.User.get_user_map_by_user_id(user_id_list)
        data = dict()
        data['find_list'] = find_list
        data['user_map'] = user_map
        return json.dumps(data)

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        add_user_id = web.input().get("user_id")
        pdbc.Friend.insert(add_user_id, user_id)
        Find.send_reminder(add_user_id, user_id)
        web.seeother('./old')

    @staticmethod
    def send_reminder(add_user_id, user_id):
        pdbc.ReminderFriend.insert(add_user_id, user_id)


app_friends = web.application(urls, locals())
