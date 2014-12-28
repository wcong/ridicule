# encoding=utf8
'''
notice page
'''

import web
import json
import config
import pdbc
import util

urls = (
    '/', 'Index'
)


class Index():
    def GET(self):
        if util.is_json_request():
            return self.get_json()
        else:
            return self.get_html()

    def get_json(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        like_list = pdbc.ReminderLike.select_reminder(user_id)
        friend_list = pdbc.ReminderFriend.select_reminder(user_id)
        comment_list = pdbc.ReminderComment.select_reminder(user_id)
        data = dict()
        data['like_list'] = like_list
        data['like_num'] = len(like_list)
        data['friend_list'] = friend_list
        data['friend_num'] = len(friend_list)
        data['comment_list'] = comment_list
        data['comment_num'] = len(comment_list)
        return json.dumps(data)

    def get_html(self):
        return config.render.notice({"hello": "world"})


app_reminder = web.application(urls, locals())