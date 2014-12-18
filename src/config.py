# encoding=utf8
__author__ = 'wcong'
import web
from wsgilog import WsgiLog, log
import sys, logging
# #
# personal log setting
class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(
            self,
            application,
            tofile=True,
            toprint=True,
            logformat='[%(asctime)s][%(name)s][%(levelname)s]: %(message)s',
            datefmt='%Y-%m-%dT%H:%M:%S',
            file='log.log',
            interval='d',
            loglevel=logging.DEBUG
        )

    def __call__(self, environ, start_response):
        def hstart_response(status, response_headers, *args):
            out = start_response(status, response_headers, *args)
            try:
                logline = environ["SERVER_PROTOCOL"] + " " + environ["REQUEST_METHOD"] + " " + environ[
                    "REQUEST_URI"] + " - " + status
            except Exception, err:
                logline = "Could not log <%s> due to err <%s>" % (str(environ), err)
            self.logger.info(logline)
            return out

        return super(Log, self).__call__(environ, hstart_response)


# #
# log time
log_time_interval = 30 * 60

# #
# config log

# web.config.log_file = 'web.log'
# web.config.log_toprint = False
# web.config.log_tofile = True

# #
# email
web.config.smtp_server = 'smtp.163.com'
web.config.smtp_port = 25
web.config.smtp_username = 'redicule@163.com'
web.config.smtp_password = 'email.redicule'
web.config.smtp_starttls = True

# #
# db
mysql = web.database(dbn="mysql", db="ridicule", user="root", pw="123", host="127.0.0.1")

# #
# host
host = '42.96.188.208:8080'

# #
# template
render = web.template.render('templates/', globals={'str': str, }, cache=False, base="layout")
