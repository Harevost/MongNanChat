#-*- coding: utf-8 -*-

import tornado.web
#from handlers import BaseHandler

class HomeHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        user_info = self.current_user
        return self.render('home.html', user_info=user_info)
