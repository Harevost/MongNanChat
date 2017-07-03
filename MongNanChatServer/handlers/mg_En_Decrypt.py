#-*- coding: utf-8 -*-
'''from Crypto.Hash import SHA
 # author: 李贇
 # description: MongNanChat Project
'''
from Crypto import Random

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import hashlib
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import string
class Message_Send(object):
    def __init__(self,text):
        self.mode=AES.MODE_CBC#AES加密模式
        self.text=text

    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def Mac_Encrypt(self,session_key):
        digest=hashlib.md5()
        digest.update(self.text)
        data=digest.hexdigest()+" "+self.text
        cryptor=AES.new(session_key,self.mode,b'0000000000000000')
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length=16
        count=len(data)
        add=length-(count%length)
        data=data+('\0'*add)
        ciphertext=cryptor.encrypt(data)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(ciphertext)
     
class Message_Recv(object):
    def __init__(self,ciphertext):
        self.mode=AES.MODE_CBC
        self.text=ciphertext

    def Decrypt_Ver(self,session_key):
        cryptor=AES.new(session_key,self.mode,b'0000000000000000')
        data=cryptor.decrypt(a2b_hex(self.text))
        plain_text=data.rstrip('\0')#解密后，去掉补足的空格用strip() 去掉
        sp=plain_text.split(' ', 1 )
        message=sp[1]
        digest=sp[0]
        check_digest=hashlib.md5()
        check_digest.update(message)
        if check_digest.hexdigest()==digest:
            return message
        else:
            return False

'''
msg=Message_Send(data)
cipher=msg.Sign_En(sk)
rec=Message_Recv(data)
msg=rec.De_Ver(sk)
'''