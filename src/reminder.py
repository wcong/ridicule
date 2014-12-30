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
        like_map = dict()
        for like in like_list:
            ridicule_id = str(like['like_ridicule_id'])
            if ridicule_id not in like_map:
                like_map[ridicule_id] = 0
            like_map[ridicule_id] += 1
        friend_list = pdbc.ReminderFriend.select_reminder(user_id)
        comment_list = pdbc.ReminderComment.select_reminder(user_id)
        comment_map = dict()
        for comment in comment_list:
            ridicule_id = str(comment['comment_ridicule_id'])
            if ridicule_id not in comment_map:
                comment_map[ridicule_id] = 0
            comment_map[ridicule_id] += 1
        ridicule_id_list = list(set(like_map.keys()).union(set(comment_map.keys())))
        ridicule_map = dict()
        if len(ridicule_id_list) > 0:
            ridicule_list = pdbc.Ridicule.select_by_batch_id(ridicule_id_list)
            for ridicule in ridicule_list:
                ridicule_map[str(ridicule['id'])] = ridicule

        data = dict()
        data['like_map'] = like_map
        data['like_num'] = len(like_list)
        data['friend_list'] = friend_list
        data['friend_num'] = len(friend_list)
        data['comment_map'] = comment_map
        data['comment_num'] = len(comment_list)
        data['ridicule_map'] = ridicule_map
        return json.dumps(data)

    def get_html(self):
        return config.render.notice({"hello": "world"})


app_reminder = web.application(urls, locals())