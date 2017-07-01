#-*- coding: utf-8 -*-

import tornado.web
import os

class OtherPageHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        username = self.get_secure_cookie('username')
        return username
    @tornado.web.authenticated
    def get(self, page):
        pagename = page + '.html'
        path = os.path.join(self.settings['static_path'], pagename)
        self.render(pagename)