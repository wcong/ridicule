# encoding=utf8
__author__ = 'wcong'
import web

import config
import util


urls = (
    '/', 'Index',
    '/write', 'Write'
)


class Index:
    def GET(self):
        return config.render.redicule()


class Write:
    def GET(self):
        return config.render.write_redicule()

    def POST(self):
        email = util.get_user_email()
        create_time = util.make_create_time()
        user_id = util.get_user_id_by_email(email)
        ridicule = web.input().get("ridicule")
        sql = 'insert into db_ridicule(create_time,user_id,content)values("' + create_time + '",' + user_id + ',"' + ridicule + '")'
        config.mysql.query(sql)


app_ridicule = web.application(urls, locals())