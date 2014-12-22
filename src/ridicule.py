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
        return config.render.ridicule(data)


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