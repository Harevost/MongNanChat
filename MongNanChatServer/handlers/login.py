#-*- coding: utf-8 -*-
import json
from handlers import BaseHandler
from pycket.session import SessionMixin

class LoginHandler(BaseHandler, SessionMixin):
    def get(self):
        return self.render('login.html')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        getInfo = 'select id from users where username="%s" and password="%s"' % (username, password)
        if username and password and self.application.db.get(getInfo):
            self.set_secure_cookie('username', self.get_argument('username', None))
            #set session
            self.session.set('user_session_test', self.get_argument('username'))
            txt = str(self.session.get('user_session_test'))
            #test session
            self.write('OK')
            #self.write('Successfully set cookie! user_session_test value: %s' % txt)
