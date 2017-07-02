#-*- coding: utf-8 -*-

import logging
import tornado.auth
import tornado.escape
import tornado.options
import tornado.web
import json
import tornado.httpserver
import tornado.websocket

#userpair = [{uidA, userA}, {uidB, userB}]
#chatpair =

class SocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_message(self, message):
        self.write_message('Your message was' + message)

    def on_close(self):
        pass
