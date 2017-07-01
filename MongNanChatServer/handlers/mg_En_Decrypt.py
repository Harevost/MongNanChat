'''
 # author: 李贇
 # describe: MongNanChat Project
'''
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class Message(object):
    def __init__(self, text, session_key, friendname):
        self.mode = AES.MODE_CBC
        self.text = text
        self.key = session_key
        self.friendname = friendname

    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def Mg_En_Sign(self):
        prikey_path="xxxxxxx"
        with open(prikey_path) as f:
            private_key = f.read()
            rsakey = RSA.importKey(private_key)
            signer = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA.new()
            digest.update(self.text)
            sign = signer.sign(digest)
            signature = base64.b64encode(sign)
        data = signature+ " " + self.text
        cryptor = AES.new(self.key, self.mode)
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(data)
        add = length - (count % length)
        data = data + ('\0' * add)
        ciphertext = cryptor.encrypt(data)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
    def Mg_De_Ver(self):
        #cryptor = AES.new(self.key, self.mode, self.key)
        cryptor = AES.new(self.key, self.mode)
        data = cryptor.decrypt(a2b_hex(self.text))
        plain_text = data.rstrip('\0')
        text = plain_text.split(' ', 1 )
        message = text[1]
        signature = text[0]
        pubkey_path = os.path.join(os.path.dirname(__file__), "public_key\\"+self.friendname+".pem")
            public_key = f.read()
            rsakey = RSA.importKey(public_key)
            verifier = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA.new()
            # Assumes the data is base64 encoded to begin with
            digest.update(message)
            is_verify = verifier.verify(digest, base64.b64decode(signature))
            if is_verify:
                return message
            else:
                return false