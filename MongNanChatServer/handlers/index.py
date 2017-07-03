#-*- coding: utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class IndexHandler(BaseHandler):

    users = set()

    @tornado.web.authenticated
    def get(self, username):
        self.render('index.html', username=self.current_user)
        userip = self.request.remote_ip
        username = self.current_user
        userport = self.request.headers['host'].replace(self.request.remote_ip + ':', '')
        print self.request.headers

        online = 'insert into entries(user_id, ip_address, port) values ("%s","%s","%s")' % (username, userip, userport)
        self.application.db.execute(online)
        self.users.add(self.current_user)
        print self.users