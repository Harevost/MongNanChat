#-*- coding: utf-8 -*-

import tornado.websocket
import json

#user_a = {“id”:1,”name”:”A”}
#user_b = {“id”:2,”name”:”B”}
#chat_a = { “id”:1, “user”:1, “who”:2, “name”:”B”, “new”:0, msg:[]}
#chat_b = { “id”:2, “user”:2, “who”:1, “name”:”A”, “new”:0, msg:[]}
#msg = { “user”:发送者id, “name”:发送者name, “date”:发送时间, “content”:消息内容 }


class SocketsHandler(tornado.websocket.WebSocketHandler):
    chats = dict()

    def open(self, user_a, user_b, chat_a, chat_b, msg):
        self.write_message(json.dump({
            'type': 'sys',
            'message': 'Welcome to MongNanChat',
        }))
        min_id = user_a['id']
        max_id = user_b['id']
        if min_id > max_id:
            min_id = user_b['id']
            max_id = user_a['id']
        key = str(min_id) + "_" + str(max_id)
        SocketsHandler.send_to_all({
            'type': 'sys',
            'message': str(id(self)) + 'has joined',
        })
        if key in SocketsHandler.chats:
            SocketsHandler.chats[key].append(self)
        else:
            SocketsHandler.chats[key] = [self]

    def close(self):
        SocketsHandler.chats.pop(self)
        SocketsHandler.send_to_all({
            'type': 'sys',
            'message': str(id(self) + 'has left'),
        })

    def send_to_all(message):
        for c in SocketsHandler.chats:
            c.write_message(json.dumps(message))

    def on_message(self, message):
        SocketsHandler.send_to_all({
            'type': 'user',
            'id': id(self),
            'message': message,
        })