# encoding=utf8
__author__ = 'wcong'
import web
import pdbc
import config
import util
import json


urls = (
    '/', 'Index',
    '/write', 'Write',
    '/like', 'Like',
    '/comment', 'Comment'
)


class Index:
    def GET(self):
        ridicule_id = web.input().get('id')
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        ridicule = pdbc.Ridicule.select_by_id(ridicule_id)
        comment_list = pdbc.Comment.select_by_ridicule_id(ridicule_id)
        comment_user_list = list()
        for comment in comment_list:
            comment_user_list.append(str(comment['user_id']))
        user_map = pdbc.User.get_user_map_by_user_id(comment_user_list)
        like_list = pdbc.Like.select_by_ridicule_id(ridicule_id)
        is_liked = False
        for like in like_list:
            if like['user_id'] == user_id:
                is_liked = True
        data = dict()
        data['ridicule'] = ridicule
        data['like_list'] = like_list
        data['like_num'] = len(like_list)
        data['comment_list'] = comment_list
        data['comment_num'] = len(comment_list)
        data['is_liked'] = is_liked
        data['user_map'] = user_map
        return config.render.ridicule(data)


class Comment:
    def POST(self):
        input = web.input()
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        ridicule_id = input.get("id")
        comment = input.get("comment")
        comment_id = pdbc.Comment.insert(user_id, ridicule_id, comment)
        ridicule = pdbc.Ridicule.select_by_id(ridicule_id)
        if ridicule['user_id'] != user_id:
            pdbc.ReminderComment.insert(ridicule['user_id'], user_id, comment_id, ridicule_id)


class Like:
    def POST(self):
        input = web.input()
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        ridicule_id = input.get("id")
        liked_list = pdbc.Like.liked_list(user_id, ridicule_id)
        data = dict()
        if len(liked_list) == 0:
            data['now'] = True
            pdbc.Like.insert(user_id, ridicule_id)
        else:
            like = liked_list[0]
            if like['is_delete'] == 0:
                data['now'] = False
                pdbc.Like.change_is_deleted(like['id'], 1)
            else:
                data['now'] = True
                pdbc.Like.change_is_deleted(like['id'], 0)
        ridicule = pdbc.Ridicule.select_by_id(ridicule_id)
        if ridicule['user_id'] != user_id:
            if data['now']:
                pdbc.ReminderLike.insert_or_update(ridicule['user_id'], user_id,ridicule_id)
            else:
                pdbc.ReminderLike.update(ridicule['user_id'], ridicule_id, 1)
        return json.dumps(data)


class Write:
    def GET(self):
        return config.render.write_ridicule()

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        ridicule = web.input().get("ridicule")
        pdbc.Ridicule.insert(user_id, ridicule)
        web.seeother('../my/')


app_ridicule = web.application(urls, locals())
