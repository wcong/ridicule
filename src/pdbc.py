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
        sql = 'select id from ' + Company.db_name + ' where is_delete = 0 and  email = "' + email + '"'
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
        sql = 'select id from ' + Position.db_name + ' where is_delete = 0 and  company_id=' + company_id + ' and name = "' + name + '"'
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
        sql = 'select id from ' + User.db_name + ' where is_delete = 0 and  email = "' + email + '"'
        data = list(db.query(sql))
        if len(data) > 0:
            return data[0]['id']

    @staticmethod
    def update_by_id(user_id, field, value):
        sql = 'update ' + User.db_name + ' set ' + field + ' = "' + value + '" where id=' + str(user_id)
        db.query(sql)

    @staticmethod
    def update_list_by_id(user_id, set_list):
        sql = 'update ' + User.db_name + ' set ' + ','.join(set_list) + ' where id=' + str(user_id)
        db.query(sql)

    @staticmethod
    def is_check_sign_same(email, check_sign):
        sql = 'select count(*) from ' + User.db_name + ' where is_delete = 0 and  email="' + email + '" and check_sign ="' + check_sign + '"'
        data = list(db.query(sql))
        if data[0]['count(*)'] > 0:
            return True
        else:
            return False

    @staticmethod
    def select_all_by_id(user_id):
        sql = 'select * from ' + User.db_name + ' where is_delete = 0 and  id=' + str(user_id)
        return list(db.query(sql))[0]

    @staticmethod
    def select_login_user(email, password):
        sql = 'select count(*) from db_user where email ="' + email + '" and password="' + util.encode_string(
            password) + '"'
        return list(db.query(sql))[0]['count(*)']

    @staticmethod
    def update_password_by_email(email, password):
        sql = 'update db_user set password="' + util.encode_string(password) + '" where email ="' + email + '"'
        db.query(sql)

    @staticmethod
    def select_by_company_id(company_id, user_id_list):
        sql = 'select id,email,nickname from ' \
              + User.db_name + \
              ' where is_delete =0 and company_id=' + str(company_id) + \
              ' and id not in (' + ','.join(user_id_list) + ')'
        return list(db.query(sql))

    @staticmethod
    def get_user_map_by_user_id(user_id_list):
        if len(user_id_list) == 0:
            return dict()
        sql = 'select id,email,nickname,is_nickname from ' \
              + User.db_name + \
              ' where is_delete =0 ' + \
              ' and id in (' + ','.join(user_id_list) + ')'
        user_list = list(db.query(sql))
        user_map = dict()
        for user in user_list:
            if user['is_nickname'] == 1:
                if user['nickname'] is None:
                    user_map[str(user['id'])] = '匿名'
                else:
                    user_map[str(user['id'])] = user['nickname']
            else:
                user_map[str(user['id'])] = user['email']
        return user_map


class Ridicule:
    db_name = 'db_ridicule'

    @staticmethod
    def select_by_user_id(user_id):
        sql = 'select id,content from ' + Ridicule.db_name + ' where is_delete = 0 and  user_id=' + str(
            user_id)
        return list(db.query(sql))

    @staticmethod
    def select_by_id(ridicule_id):
        sql = 'select id,user_id,content from ' + Ridicule.db_name + ' where is_delete = 0 and  id=' + str(
            ridicule_id)
        return list(db.query(sql))[0]

    @staticmethod
    def get_ridicule_by_user_id_list(user_id_list):
        sql = 'select id,user_id,content from db_ridicule where user_id in (' + ','.join(
            user_id_list) + ') order by create_time desc'
        data = list(db.query(sql))
        return data

    @staticmethod
    def insert(user_id, ridicule):
        sql = 'insert into db_ridicule(create_time,user_id,content)values("' + util.make_create_time() + '",' + str(
            user_id) + ',"' + ridicule + '")'
        db.query(sql)

    @staticmethod
    def select_by_batch_id(ridicule_id_list):
        sql = 'select id,content from ' + Ridicule.db_name + \
              ' where id in (' + ','.join(ridicule_id_list) + ') and is_delete = 0'
        return list(db.query(sql))


class Like:
    db_name = 'db_like'

    @staticmethod
    def select_by_ridicule_id(ridicule_id):
        sql = 'select id,user_id from ' + Like.db_name + ' where is_delete = 0 and  ridicule_id=' + str(ridicule_id)
        return list(db.query(sql))

    @staticmethod
    def liked_list(user_id, ridicule_id):
        sql = 'select id,user_id,is_delete from ' + Like.db_name + ' where user_id=' + str(
            user_id) + ' and ridicule_id=' + str(ridicule_id)
        return list(db.query(sql))

    @staticmethod
    def insert(user_id, ridicule_id):
        sql = 'insert into ' + Like.db_name + \
              '(create_time,ridicule_id,user_id)values("' + \
              util.make_create_time() + '",' + str(ridicule_id) + ',' + str(user_id) + ')'
        db.query(sql)

    @staticmethod
    def change_is_deleted(like_id, is_deleted):
        sql = 'update ' + Like.db_name + \
              ' set is_delete=' + str(is_deleted) + \
              ' where id=' + str(like_id)
        db.query(sql)


class Comment:
    db_name = 'db_comment'

    @staticmethod
    def select_by_ridicule_id(ridicule_id):
        sql = 'select id,user_id,content from ' + Comment.db_name + ' where is_delete = 0 and ridicule_id=' + str(
            ridicule_id)
        return list(db.query(sql))

    @staticmethod
    def insert(user_id, ridicule_id, comment):
        return db.insert(Comment.db_name,
                         create_time=util.make_create_time(),
                         user_id=user_id,
                         ridicule_id=ridicule_id,
                         content=comment)


class Friend:
    db_name = 'db_friend'

    @staticmethod
    def select_by_user_id(user_id):
        sql = 'select id,related_user_id,is_open from ' + Friend.db_name + \
              ' where is_delete = 0 and main_user_id=' + str(user_id)
        return list(db.query(sql))

    @staticmethod
    def select_user_id_by_user_id(user_id):
        sql = 'select related_user_id from ' + Friend.db_name + ' where is_delete = 0 and main_user_id=' + str(user_id)
        return list(db.query(sql))

    @staticmethod
    def select_main_user_id_by_user_id(user_id):
        sql = 'select main_user_id from ' + Friend.db_name + ' where is_delete = 0 and related_user_id=' + str(user_id)
        return list(db.query(sql))

    @staticmethod
    def select_open_friends_by_user_id(user_id):
        sql = 'select related_user_id from ' + Friend.db_name + ' where is_delete = 0 and main_user_id=' + str(
            user_id) + ' and is_open =1'
        return list(config.mysql.query(sql))

    @staticmethod
    def insert(main_id, add_id):
        sql = 'insert into ' + Friend.db_name + \
              '(create_time,main_user_id,related_user_id)' \
              'values' \
              '("' + util.make_create_time() + '",' + str(main_id) + ',' + str(add_id) + ')'
        db.query(sql)

    @staticmethod
    def update_is_open(friend_id, is_open):
        sql = 'update ' + Friend.db_name + \
              ' set is_open=' + str(is_open) + \
              ' where id = ' + str(friend_id)
        db.query(sql)


class ReminderFriend:
    db_name = 'db_reminder_friend'

    @staticmethod
    def insert(user_id, request_user_id):
        sql = 'insert into ' + ReminderFriend.db_name + \
              '(create_time,user_id,request_user_id)values' \
              '("' + util.make_create_time() + '",' + str(user_id) + ',' + str(request_user_id) + ')'
        db.query(sql)

    @staticmethod
    def select_reminder(user_id):
        sql = 'select request_user_id from ' + ReminderFriend.db_name + \
              ' where user_id= ' + str(user_id) + ' and is_read = 0'
        return list(db.query(sql))

    @staticmethod
    def clear_reminder(user_id):
        sql = 'update ' + ReminderFriend.db_name + \
              ' set is_read = 1 where user_id=' + str(user_id)
        db.query(sql)


class ReminderComment:
    db_name = 'db_reminder_comment'

    @staticmethod
    def insert(user_id, comment_user_id, comment_id, ridicule_id):
        return db.insert(ReminderComment.db_name,
                         create_time=util.make_create_time(),
                         user_id=user_id,
                         comment_user_id=comment_user_id,
                         comment_id=comment_id,
                         comment_ridicule_id=ridicule_id)

    @staticmethod
    def select_reminder(user_id):
        sql = 'select comment_ridicule_id,comment_user_id,comment_id from ' + ReminderComment.db_name + \
              ' where user_id=' + str(user_id) + ' and is_read = 0'
        return list(db.query(sql))

    @staticmethod
    def clear_reminder(ridicule_id):
        sql = 'update ' + ReminderComment.db_name + \
              ' set is_read = 1 where comment_ridicule_id=' + str(ridicule_id)
        db.query(sql)


class ReminderLike:
    db_name = 'db_reminder_like'

    @staticmethod
    def insert_or_update(user_id, like_user_id, ridicule_id):
        data = ReminderLike.select(ridicule_id, like_user_id)
        if len(data) == 0:
            return db.insert(ReminderLike.db_name,
                             create_time=util.make_create_time(),
                             user_id=user_id,
                             like_ridicule_id=ridicule_id,
                             like_user_id=like_user_id)
        else:
            ReminderLike.update(ridicule_id, like_user_id, 0)


    @staticmethod
    def select(ridicule_id, like_user_id):
        sql = 'select id from ' + ReminderLike.db_name + \
              ' where ' \
              'like_ridicule_id=' + str(ridicule_id) + ' and like_user_id=' + str(like_user_id)
        return list(db.query(sql))

    @staticmethod
    def select_reminder(user_id):
        sql = 'select id,like_ridicule_id,like_user_id from ' + ReminderLike.db_name + \
              ' where user_id=' + str(user_id) + ' and is_read = 0'
        return list(db.query(sql))

    @staticmethod
    def update(ridicule_id, like_user_id, is_read):
        sql = 'update ' + ReminderLike.db_name + \
              ' set is_read = ' + str(is_read) + \
              ' where like_ridicule_id=' + str(ridicule_id) + ' and like_user_id=' + str(like_user_id)
        db.query(sql)

    @staticmethod
    def clear_reminder(ridicule_id):
        sql = 'update ' + ReminderLike.db_name + \
              ' set is_read=1 where like_ridicule_id = ' + str(ridicule_id)
        db.query(sql)


class Boycott:
    db_name = 'db_boycott'

    @staticmethod
    def insert(user_id, content):
        return db.insert(Boycott.db_name,
                         create_time=util.make_create_time(),
                         user_id=user_id,
                         content=content)


class BoycottLike:
    db_name = 'db_boycott_like'

    @staticmethod
    def insert(boycott_id, like_user_id):
        return db.insert(BoycottLike.db_name,
                         create_time=util.make_create_time(),
                         boycott_id=boycott_id,
                         like_user_id=like_user_id)


class BoycottComment:
    db_name = 'db_boycott_comment'

    @staticmethod
    def insert(boycott_id, comment_user_id, comment):
        return db.insert(BoycottComment.db_name,
                         create_time=util.make_create_time(),
                         boycott_id=boycott_id,
                         comment_user_id=comment_user_id,
                         content=comment)





