#-*- coding: utf-8 -*-

import errno
import functools
from tornado.ioloop import IOLoop
import socket
import time
import Queue

sock = socket.socket    (socket.AF_INET,socket.SOCK_STREAM,0)
sock.setblocking(0)
server_address = ("10.21.225.35", 12450)
sock.bind(server_address)
sock.listen(10)

fd_map = {}
message_queue_map = {}

fd = sock.fileno()
fd_map[fd] = sock

ioloop = IOLoop.instance()

def handle_client(cli_addr,fd, event):
    print event, IOLoop.WRITE
    s=fd_map[fd]
    if event & IOLoop.READ: #receive the data
        data = s.recv(1024)
        if data:
            print"receive %s from %s" %(data,cli_addr)
            ioloop.update_handler(fd, IOLoop.WRITE)
            message_queue_map[s].put(data)
        else:
            print "closing %s  " %cli_addr
            ioloop.remove_handler(fd)
            s.close()
            del message_queue_map[s]
    if event & IOLoop.WRITE:
        try:
            next_msg= message_queue_map[s].get_nowait   ()
        except Queue.Empty:
            print"%s Queue Empty"% cli_addr
            ioloop.update_handler(fd,IOLoop.READ)   #CHANGE THE SITUATION
        else:
            print"sending %s to %s " % (next_msg,   cli_addr)
            s.send(next_msg)
            ioloop.update_handler(fd,IOLoop.READ)#
    if event &IOLoop.ERROR:
        print"%s EXCEPTION ON" % cli_addr
        ioloop.remove_handler(fd)
        s.close()
        del message_queue_map[s]

def handle_server(fd,event):
    s = fd_map[fd]
    if event & IOLoop.READ:
        get_connection,cli_addr = s.accept()
        print"connection %s " % cli_addr[0]
        get_connection.setblocking(0)
        get_connection_fd = get_connection.fileno()
        fd_map[get_connection_fd] = get_connection
        handle = functools.partial  (handle_client,cli_addr[0])
        ioloop.add_handler(get_connection_fd,handle,IOLoop.READ)
        message_queue_map[get_connection] = Queue.Queue()
io_loop = IOLoop.instance()
io_loop.add_handler(fd,handle_server,io_loop.READ)
try:
    io_loop.start()
except KeyboardInterrupt:
    print "exit"
    io_loop.stop()

