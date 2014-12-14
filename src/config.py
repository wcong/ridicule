# encoding=utf8
__author__ = 'wcong'
import web

# #
# log time
log_time_interval = 30 * 60

# #
# email
web.config.smtp_server = 'smtp.163.com'
web.config.smtp_port = 587
web.config.smtp_username = 'redicule@163.com'
web.config.smtp_password = 'email.redicule'
web.config.smtp_starttls = True

# #
# db
mysql = web.database(dbn="mysql", db="redicule", user="root", pw="123", host="127.0.0.1")

# #
# host
host = '42.96.188.208'

##
# template
render = web.template.render('templates/', cache=False, base="layout")