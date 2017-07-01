#-*- coding: utf-8 -*-

import binascii
import tornado.web
import os

class BaseHandler(tornado.web.RequestHandler):
    # class static var are used to save login info, user_id <-> token

    __TOKEN_LIST = {}

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def new_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16))
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def on_login_success(self, new_token, user_id):
        self.set_cookie('_token', new_token)
        self.__TOKEN_LIST[new_token] = user_id

    def get_current_user(self):
        #cookie中读取token
        token = self.get_cookie('_token')

        #根据token得到对应user_id
        if token and token in self.__TOKEN_LIST:
            user_id = self.__TOKEN_LIST[token]
            return self.application.user_list[user_id]

        #未登录
        return None