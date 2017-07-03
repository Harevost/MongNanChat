#-*- coding: utf-8 -*-
import json

import tornado.web
from handlers.index import BaseHandler
from Crypto.Hash import SHA

class LoginHandler(BaseHandler):

    def get(self):
        return self.render('login.html')

    def post(self):
        log_reg_flag = self.get_argument('log_reg_flag')
        if log_reg_flag == '1':
            username = self.get_argument('username', None)
            password = self.get_argument('password', None)
            pwd_hash = SHA.SHA1Hash(password).hexdigest()
            getInfo = 'select id from users where username="%s" and pwd_hash="%s"' % (username, pwd_hash)
            if username and password and self.application.db.get(getInfo):
                self.set_secure_cookie('username', self.get_argument('username'))
                self.write("1")
        elif log_reg_flag == '0':
            username = self.get_argument('username')
            password = self.get_argument('password')
            email = self.get_argument('email')
            #public_key = self.get_argument('public_key')

            if self.application.db.get('select id from users where username="%s"' % username):
                self.write("0")
            else:
                pwd_hash = SHA.SHA1Hash(password).hexdigest()
                insert = 'insert into users (username, email, pwd_hash) values ("%s","%s","%s")' % (username, email, pwd_hash)
                self.application.db.execute(insert)
                #with open('%s' % username + '.pem', 'w') as f:
                #    f.write(public_key)
                self.write("1")

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('logout.html')
        offline = 'delete from entries where user_id="%s"' % self.current_user
        self.application.db.execute(offline)