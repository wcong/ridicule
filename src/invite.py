# encoding=utf8
__author__ = 'wcong'

import json

import web

import util

import config
import pdbc


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
        register_link = 'http://' + config.host + '/register/?email=' + register_link_meta[0] + '&sign=' + \
                        register_link_meta[1]
        Index.select_or_add_email(email, register_link_meta[1])
        message = '<html xmlns=\'http://www.w3.org/1999/xhtml\'><body><h1>click the follow links</h1><a href="' + register_link + '">click to register</a></body></html>'
        web.sendmail('redicule@163.com', email, 'register', message,
                     headers={'Content-Type': 'text/html;charset=utf-8'})
        result = dict()
        result['success'] = True
        return json.dumps(result)

    @staticmethod
    def select_or_add_email(email, check_sign):
        user_id = pdbc.User.select_id_by_email(email)
        if user_id is not None:
            pdbc.User.update_by_id(str(user_id), 'check_sign', check_sign)
            return
        company_email = util.extract_company_from_email(email)
        company_id = pdbc.Company.select_id_by_email(company_email)
        if company_id is None:
            pdbc.Company.insert_by_email(company_email)
            company_id = pdbc.Company.select_id_by_email(company_email)
            pdbc.Position.init_company(str(company_id))
        position_id = pdbc.Position.select_id_by_company(str(company_id))
        pdbc.User.init_user(email, check_sign, str(company_id), str(position_id))


app_invite = web.application(urls, locals())
