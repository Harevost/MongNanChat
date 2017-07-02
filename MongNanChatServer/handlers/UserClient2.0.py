#coding=utf-8

from socket import *
import sk_Agreement
import mg_En_Decrypt

HOST = 'localhost'
PORT = 21578
BUFSIZE = 1024
ADDR = (HOST, PORT)

ClientSock = socket(AF_INET, SOCK_STREAM)
ClientSock.connect(ADDR)

#首先进行一次密钥协商

sk = sk_Agreement.sessionKey_En()
cipher_sk = sk.encrypt()
ClientSock.send(cipher_sk)

#然后对信息进行加密后发送

while True:
    #加密消息并发送
    data = raw_input('>')
    if not data:
        break
    msg = mg_En_Decrypt.Message_Send(data)
    cipher = msg.Mac_En(sk.session_key)
    print '已加密数据为' + cipher#已加密数据
    ClientSock.send(cipher)

    #接收消息并解密
    data = ClientSock.recv(BUFSIZE)
    if not data:
        break
    print '为解密数据为' + data#未解密数据
    rec = mg_En_Decrypt.Message_Recv(data)
    data = rec.De_Ver(sk.session_key)
    print data

ClientSock.close()