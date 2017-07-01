#-*- coding: utf-8 -*-

import tornado.web

class HeaderBar(tornado.web.UIModule):
    def render(self, location):
        return self.render_string("header.html")

class HeaderBarWithLocation(tornado.web.UIModule):
    def render(self, location):
        return self.render_string("header.html", location=location)