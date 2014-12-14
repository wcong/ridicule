__author__ = 'wcong'
import base64
import datetime

import web

import config


'''
this is util function of web app
'''


def make_register_link(email):
    return base64.encode(email), base64.encode(email + '' + str(datetime.datetime.now().time()))


def get_user_email():
    return decode_string(web.cookies().get("email"))


def get_user_id_by_email(email):
    sql = 'select id from db_user where email = "' + email + '"'
    data = list(config.mysql.query(sql))
    return data[0]['id']


def encode_string(string):
    return base64.encodestring(string)


def decode_string(string):
    return base64.decodestring(string)

def make_create_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")