#coding=utf-8
from socket import *
from time import ctime
import threading
from time import sleep
import sk_Agreement
import  mg_En_Decrypt


HOST = ''
PORT = 21578
BUFSIZE = 1024
ADDR=(HOST, PORT)

ServerSock=socket(AF_INET, SOCK_STREAM)
ServerSock.bind(ADDR)
ServerSock.listen(5)

def response(ClientSock, addr):
    print '... connected from:', addr

    # 首先进行一次密钥协商

    cipher_sk = ClientSock.recv(BUFSIZE)
    _sk = sk_Agreement.sessionKey_De(cipher_sk)
    sk = _sk.decrypt()

    while True:

        #解密接收到的客户端发来的消息
        data = ClientSock.recv(BUFSIZE)
        if not data:
            break
        rec = mg_En_Decrypt.Message_Recv(data)
        data = rec.De_Ver(sk.session_key)
        print data
        #加密消息并发送
        data = raw_input('>')
        if not data:
            break
        msg = mg_En_Decrypt.Message_Send(data)
        cipher = msg.Mac_En(sk.session_key)
        ClientSock.send(cipher)
        print data



while True:
    sleep(0.1)
    print 'waiting for connection ...'
    ClientSock,addr = ServerSock.accept()
    t = threading.Thread(target=response, args=(ClientSock, addr))
    t.start()


ClientSock.close()
ServerSock.close()