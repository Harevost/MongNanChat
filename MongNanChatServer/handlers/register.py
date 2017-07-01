#-*- coding: utf-8 -*-

import tornado.web
import tornado.autoreload

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        email = self.get_argument('email')
        pwd_confirm = self.get_argument('confirm')
        print('select id from users where username = "%s"' % username)

        if (not password) or (not pwd_confirm):
            self.write('password is empty!')
        elif not email:
            self.write('email is empty')
        elif not username:
            self.write('username is empty!')
        elif pwd_confirm != password:
            self.write('password is not same!')

        elif self.application.db.get('select id from users where name="%s"' % username):
            self.write('user already exists')
        else:
            random_generator = Random.new().read
            rsa = RSA.generate(1024, random_generator)
            pwd_hash = SHA.SHA1Hash(password)
            private_key = rsa.exportKey()
            with open(username + '_pri.pem', 'w') as f:
                f.write(private_key)
            public_key = rsa.publickey().exportkey()
            with open(username + '_pub.pem', 'w') as f:
                f.write(public_key)
            insert = 'insert into users (username, email, pwd_hash, public_key) values ("%s","%s","%s","%s")' \
                     % (username, email, pwd_hash, public_key)
            self.application.db.execute(insert)
            self.write('Registered successfully')
            #用户注册成功，用随机数生成RSA公私钥对，公钥传至服务器，私钥传至本地



