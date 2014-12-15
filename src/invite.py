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
        message = '<html xmlns=\'http://www.w3.org/1999/xhtml\'><body><h1>click the follow links</h1><a href="' + register_link + '">click to register</a></body></html>'
        web.sendmail('redicule@163.com', email, 'register', message,
                     headers={'Content-Type': 'text/html;charset=utf-8'})
        result = dict()
        result['success'] = True
        return json.dumps(result)

    @staticmethod
    def select_or_add_email(email):
        sql = 'select id from db_user where email = "' + email + '"'
        data = list(config.mysql.query(sql))
        if len(data) > 0:
            return data[0]['id']
        sql = 'insert into db_user(create_time,email)'


app_invite = web.application(urls, locals())