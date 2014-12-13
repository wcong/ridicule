#!/usr/bin/env python
# encoding=utf8

import web

'''
ok this is our main page
'''

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return "hello world"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

