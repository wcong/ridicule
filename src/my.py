# encoding=utf8
__author__ = 'wcong'

import web
import config

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return config.render.my()


app_my = web.application(urls, locals())