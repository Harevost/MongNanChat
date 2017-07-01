#-*- coding: utf-8 -*-

import tornado.web
import tornado.autoreload

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        email = self.get_argument('email')
        pwd_confirm = self.get_argument('confirm')
        print('select id from users where username = "%s"' % username)

        if (not password) or (not pwd_confirm):
            self.write('password is empty!')
        elif not email:
            self.write('email is empty')
        elif not username:
            self.write('username is empty!')
        elif pwd_confirm != password:
            self.write('password is not same!')

        elif self.application.db.get('select id from users where name="%s"' % username):
            self.write('user already exists')
        else:
            insert = 'insert into users (username, email, password) values ("%s","%s","%s")' % (username, email, password)
            self.application.db.execute(insert)
            self.write('Registered successfully')