#-*- coding: utf-8 -*-
'''
 # author: 李贇
 # description: MongNanChat Project
'''
import string
import random
import os
import base64
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

class SessionKey(object):
    def __init__(self, friendname):
        self.friendname = friendname

    def Sk_Encrypt(self):
        pubkey_path=os.path.join(os.path.dirname(__file__), "public_key\\"+self.friendname+".pem")
        with open(pubkey_path) as f:
            session_key = "".join(random.choice(string.letters+string.digits) for i in range(16))
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            cipher_SessionKey = base64.b64encode(cipher.encrypt(session_key))
        return cipher_SessionKey

    def Sk_Decrypt(self, encrypt_text):
        prikey_path = "xxxxxxx"
        with open(prikey_path) as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsakey)
            session_key = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
        return session_key