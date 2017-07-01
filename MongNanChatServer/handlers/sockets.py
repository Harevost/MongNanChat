#-*- coding: utf-8 -*-

import tornado.websocket
import json

class SocketsHandler(tornado.websocket.WebSocketHandler):
    chats = dict()

    def open(self, user_a, user_b, chat_a, chat_b):
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