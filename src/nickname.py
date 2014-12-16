# encoding=utf8
__author__ = 'wcong'

import config
import web

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return config.render.nickname()


app_nickname = web.application(urls, locals())