#-*- coding: utf-8 -*-
import json
#from handlers import BaseHandler
import tornado.web
from pycket.session import SessionMixin
from Crypto.Hash import SHA

class LoginHandler(tornado.web.RequestHandler, SessionMixin):

    def get(self):
        return self.render('login.html')

    def post(self):
        log_reg_flag = self.get_argument('log_reg_flag')
        print 'log_reg_flag:' + log_reg_flag + str(type(log_reg_flag))
        if log_reg_flag == '1':
            username = self.get_argument('username', None)
            print 'username:' + username
            password = self.get_argument('password', None)
            print 'password:' + password
            pwd_hash = SHA.SHA1Hash(password).hexdigest()
            print 'pwd_hash' + str(pwd_hash)
            getInfo = 'select id from users where username="%s" and pwd_hash="%s"' % (username, pwd_hash)
            if username and password and self.application.db.get(getInfo):
                self.set_secure_cookie('username', self.get_argument('username', None))
                self.session.set('user_session_test', self.get_argument('username'))
                txt = str(self.session.get('user_session_test'))
                self.write("1")
        elif log_reg_flag == '0':
            username = self.get_argument('username')
            password = self.get_argument('password')
            email = self.get_argument('email')

            if self.application.db.get('select id from users where username="%s"' % username):
                self.write("0")
            else:
                pwd_hash = SHA.SHA1Hash(password).hexdigest()
                insert = 'insert into users (username, email, pwd_hash) values ("%s","%s","%s")' % (username, email, pwd_hash)
                self.application.db.execute(insert)
                self.write("1")