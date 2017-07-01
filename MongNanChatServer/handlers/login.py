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
            self.write('Successfully set cookie! user_session_test value: %s' % txt)


        # get login info from body of post
        #req_data = json.loads(self.request.body.decode())
        #login = req_data['login']
        #password = req_data['password']
        # test username & password
        #login_user_id = None
        #for user_id in self.application.user_list:
        #   if login == self.application.user_list[user_id]['login']:
        #        login_user_id = user_id
        #        break
        #if not login_user_id:
        #    return self.finish('Invalid username or password')

        #if password != self.application.user_list[login_user_id]['password']:
        #    return self.finish('Invalid username or password')

        #a token a logged user
        #new_token = self.new_token()
        #self.on_login_success(new_token, login_user_id)

        #return self.finish('ok')