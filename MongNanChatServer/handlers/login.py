#-*- coding: utf-8 -*-
import json
from handlers import BaseHandler
from pycket.session import SessionMixin
from Crypto.Hash import SHA

class LoginHandler(BaseHandler, SessionMixin):
    def get(self):
        return self.render('login.html')

    def post(self):
        log_reg_flag = self.get_argument('log_reg_flag')
        if log_reg_flag:
            username = self.get_argument('username', None)
            password = self.get_argument('password', None)
            pwd_hash = SHA.SHA1Hash(password)
            getInfo = 'select id from users where username="%s" and pwd_hash="%s"' % (username, pwd_hash)
            if username and password and self.application.db.get(getInfo):
                self.set_secure_cookie('username', self.get_argument('username', None))
                self.session.set('user_session_test', self.get_argument('username'))
                txt = str(self.session.get('user_session_test'))
                self.write('ok')
        else:
            username = self.get_argument('username')
            password = self.get_argument('password')
            email = self.get_argument('email')
            pwd_confirm = self.get_argument('pwd_confirm')

            print '--debug--RegisterHandler--'
            print username
            print password
            print email

            if self.application.db.get('select id from users where name="%s"' % username):
                self.write('exists')
            else:
                pwd_hash = SHA.SHA1Hash(password)

                insert = 'insert into users (username, email, pwd_hash) values ("%s","%s","%s")' % (
                username, email, pwd_hash)
                self.application.db.execute(insert)
                self.write('ok')