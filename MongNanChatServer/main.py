import os
#import UImodules
import tornado.httpserver
import tornado.ioloop
import tornado.web
import MySQLdb
import torndb
import subprocess

from handlers.home import HomeHandler
from handlers.otherpage import OtherPageHandler
from handlers.login import LoginHandler
from handlers.sockets import SocketsHandler
from tornado.options import define, options

define('port', default=12450, help='Run on the given port', type=int)
define('debug', default=False, help='Set debug mode', type=bool)
define('mysql_host', default='127.0.0.1:3306', help='mysql host IP')
define('mysql_user', default='root', help='db user name')
define('mysql_password', default='1qazxsw2', help='db password')
define('mysql_database', default='UserInfo', help='db name')

class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Oops. This page is not found.")

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/", tornado.web.RedirectHandler, {"url": "/home"}),
            (r"/home", HomeHandler),
            (r"/login", LoginHandler),
            (r"/soc", SocketsHandler),
            (r"/(.+?)", OtherPageHandler),
            (r".*", PageNotFoundHandler),
        ]

        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            #'ui_modules': UImodules
            'cookie_secret': 'WEIZAIMABUZAICMNFNNDPGUNAOPENTHEGAYMRQUIN',
            'login_url': '/login',
            'xsrf_cookies': False,
            'debug': True,
            'pycket': {
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    'db_sessions': 10,
                    'db_notifications': 11,
                    'max_connections': 2**31,
                },
                'cookies': {
                    'expires_days': 2,
                    'expires': None,
                },
            },
        }

        super(Application, self).__init__(handlers, **settings)

        self.db = torndb.Connection("127.0.0.1:3306", "UserInfo", user="root", password="1qazxsw2")

        self.db.execute("drop table if exists entries")
        self.db.execute("drop table if exists users")
        self.db.execute("drop table if exists friends")

        self.db.execute(
            "create table entries("
            "id int not null auto_increment primary key,"
            "user_id varchar(100) not null references users(username),"
            "ip_address varchar(100) not null,"
            "port varchar(100) not null)"
        )

        self.db.execute(
            "create table users("
            "id int not null auto_increment primary key,"
            "username varchar(100) not null,"
            "email varchar(100) not null,"
            "pwd_hash varchar(100) not null,"
            "public_key varchar(100) not null)"
        )

        self.db.execute(
            "create table friends("
            "id int not null auto_increment primary key,"
            "username varchar(100) not null references users(username),"
            "friendname varchar(100) not null references users(username))"
        )

if __name__ == "__main__":
    port = 12450
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(port)

    print('Listen on http://localhost:{0}'.format(port))
    tornado.ioloop.IOLoop.instance().start()