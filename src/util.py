__author__ = 'wcong'
import base64
import datetime
import time
import web
import config


'''
this is util function of web app
'''


def make_register_link(email):
    return encode_string(email), encode_string(email + str(make_time_stamp()))


def make_time_stamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


def get_user_email():
    return decode_string(web.cookies().get("email"))


def encode_string(string):
    return base64.encodestring(string)


def decode_string(string):
    return base64.decodestring(string)


def make_create_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def extract_company_from_email(email):
    email_array = email.split('@')
    return email_array[len(email_array) - 1]