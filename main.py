#!/usr/bin/env python
# encoding=utf8

import sys

import web

reload(sys)
sys.setdefaultencoding('utf-8')

'''
ok this is our main page
'''

urls = (
    '/', 'Index'
)
web.config.debug = True
render = web.template.render('templates/', globals={'str': str}, base="index_layout", cache=False)


def login_hook(handle):
    web.cookies().get("login")


class Index:
    def GET(self):
        return render.index()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.add_processor(login_hook)
    app.run()

