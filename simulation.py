#author : Aryan Kaushik 19BCT0067
from securefile import Encrypt
from securefile.keyset import RSA_KEY, DES_KEY, AES_KEY

des_key = DES_KEY.genrate('12345678123456781234567812345678')
aes_key = AES_KEY.genrate('700102030405060708090a0b0c0d0e0f')
rsa_public_key = RSA_KEY.public_key_genrate(18285, 57067)
rsa_private_key = RSA_KEY.private_key_genrate(6861, 57067)
chiper_shift = 3

enc = Encrypt('text.txt', delimiter=':')
enc.open()

enc.base64_encrypt()
enc.aes_encrypt(aes_key, commit=True)
enc.des_encrypt(des_key, commit=True)
enc.rsa_encrypt(rsa_private_key, commit=True)
enc.caesar_cipher(key_shift=chiper_shift, commit=True)

enc.caesar_decipher(key_shift=chiper_shift, commit=True)
enc.rsa_decrypt(rsa_public_key, commit=True)
enc.des_decrypt(des_key, commit=True)
enc.aes_decrypt(aes_key, commit=True)
enc.base64_decrypt(commit=True)