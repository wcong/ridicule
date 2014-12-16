# encoding=utf8
__author__ = 'wcong'

import config
import web

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return config.render.friends()


app_friends = web.application(urls, locals())