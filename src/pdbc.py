# encoding=utf8
__author__ = 'wcong'

import config
import util


'''
this is method of db
'''

db = config.mysql


class Company:
    db_name = 'db_company'

    @staticmethod
    def insert_by_email(email):
        sql = 'insert into ' + \
              Company.db_name + \
              ' (create_time,name,email)values' \
              '("' + util.make_create_time() + '","' + email + '","' + email + '")'
        db.query(sql)

    @staticmethod
    def select_id_by_email(email):
        sql = 'select id from ' + Company.db_name + ' where email = "' + email + '"'
        data = list(db.query(sql))
        if len(data) > 0:
            return data[0]['id']


class Position:
    db_name = 'db_position'

    @staticmethod
    def init_company(company_id):
        sql = 'insert into ' \
              + Position.db_name + \
              '(create_time,company_id)values' \
              '("' + util.make_create_time() + '",' + company_id + ')'
        db.query(sql)

    @staticmethod
    def select_id_by_company(company_id, name='public'):
        sql = 'select id from ' + Position.db_name + ' where company_id=' + company_id + ' and name = "' + name + '"'
        data = list(db.query(sql))
        if len(data) > 0:
            return data[0]['id']


class User:
    db_name = 'db_user'

    @staticmethod
    def init_user(email, check_sign, company_id, position_id):
        create_time = util.make_create_time()
        sql = 'insert into ' \
              + User.db_name + \
              '(create_time,email,company_id,position_id,check_sign,register_date)values' \
              '("' + create_time + '","' + email + '",' + company_id + ',' + position_id + ',"' + check_sign + '","' + create_time + '")'
        db.query(sql)

    @staticmethod
    def select_id_by_email(email):
        sql = 'select id from ' + User.db_name + ' where email = "' + email + '"'
        data = list(db.query(sql))
        if len(data) > 0:
            return data[0]['id']

    @staticmethod
    def update_by_id(user_id, field, value):
        sql = 'update ' + User.db_name + ' set ' + field + ' = "' + value + '" where id=' + user_id
        db.query(sql)

    @staticmethod
    def is_check_sign_same(email, check_sign):
        sql = 'select count(*) from ' + User.db_name + ' where email="' + email + '" and check_sign ="' + check_sign + '"'
        data = list(db.query(sql))
        if len(data) > 0:
            return True
        else:
            return False


