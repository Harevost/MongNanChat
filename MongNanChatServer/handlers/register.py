#-*- coding: utf-8 -*-

import tornado.web
from Crypto.Hash import SHA

class RegisterHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        email = self.get_argument('email')
        pwd_confirm = self.get_argument('confirm')

        print '--debug--RegisterHandler--'
        print username
        print password
        print email


        if self.application.db.get('select id from users where name="%s"' % username):
            self.write('exists')
        else:
            pwd_hash = SHA.SHA1Hash(password)

            insert = 'insert into users (username, email, pwd_hash) values ("%s","%s","%s")' % (username, email, pwd_hash)
            self.application.db.execute(insert)
            self.write('ok')



