#-*- coding: utf-8 -*-
'''
 # author: 李贇
 # description: MongNanChat Project
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/addFriend/", AddFriendHandler), (r"/deleteFriend/(\w+)", DeleteFriendHandler)]
        conn = pymongo.Connection("localhost", 27017)
        self.db = conn["UserInfo"]
        tornado.web.Application.__init__(self, handlers, debug=True)

class AddFriendHandler(tornado.web.RequestHandler):
    def post(self):
        _friendname = self.get_argument("friendname")
        users_table = self.application.db.users
        result = users_table.find_one({"username": _friendname})
        if result:
        	friends_table = self.application.db.friends
        	relation = {"username":  , "friendname": _friendname}
            friends_table.insert(relation)
        else:
            self.write({"Oooops！输入的好友用户名不存在"})

class DeleteFriendHandler(tornado.web.RequestHandler):
    def get(self):
        _friendname = self.get_argument("friendname")
        users_table = self.application.db.users
        relation = users_table.find_one({"username": , "friendname":_friendname})
        del relation


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()