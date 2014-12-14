# encoding=utf8
__author__ = 'wcong'

import json

import web

import util

import config


urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return config.render.invite()

    def POST(self):
        input = web.input()
        if 'email' not in input:
            web.seeother('/invite')
        email = input.get("email")
        register_link_meta = util.make_register_link(email)
        register_link = 'http://' + config.host + '/register?email=' + register_link_meta[0] + '&sign=' + \
                        register_link_meta[1]
        message = '<h1>click the follow links</h2><p>' + register_link + '</p>'
        web.sendmail('redicule@163.com', email, 'register', message)
        result = dict()
        result['success'] = True
        return json.dumps(result)


app_invite = web.application(urls, locals())