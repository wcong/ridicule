# encoding=utf8
__author__ = 'wcong'

import web

import config


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return config.render.setting()


app_setting = web.application(urls, locals())