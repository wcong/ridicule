__author__ = 'wcong'
import base64
import datetime

'''
this is util function of web app
'''


def make_register_link(email):
    return base64.encode(email), base64.encode(email + '' + str(datetime.datetime.now().time()))
