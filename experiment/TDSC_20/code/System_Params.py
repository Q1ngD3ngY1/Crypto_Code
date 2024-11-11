'''该模块实现整个算法的基本函数模块'''
import base64
import binascii
import hashlib
import random
import paillier_variant

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

'''参数'''
q = 115792089237316195423570985008687907852837564279074904382605163141518161494337          #可对应到论文里的l,如果因为太大而导致变慢,可以换个小点的值来生成随机值
#AES加密的对称密钥
symmetric_key = 'woshililinhahaha'.encode()
#用户列表
U_ID = [1,2,3,4,5]
#任务列表
Mission = [1,2,3,4,5]
#paillier变体加密的公私钥
paillier_public_key = paillier_variant.public_key
paillier_private_key = paillier_variant.private_key
#print(paillier_public_key[0],'\n',paillier_public_key[1])
#print(paillier_private_key[0],'\n',paillier_private_key[1])

'''基本功能函数'''
#随机数生成函数
def rand_from_group(p):
    number = random.randint(1,p-1)
    return number

#哈希映射
def hash_to_group(message,p):
    hash_int = int(hashlib.sha256(str(message).encode()).hexdigest(),16)
    hash_int_modp = hash_int % p
    return hash_int_modp

#消息完整性检测函数
def MAC(message,z_k):
    s = str(message) + str(z_k)
    mac = hash_to_group(s,q)
    return mac

#身份认证函数
def Identity_check(h_j_1,h_j):
    h = hash_to_group(h_j,q)
    if h == h_j_1:
        return 1
    else:
        return 0
'''
m = 'I am Lilin'
h_j = hash_to_group(m,q)
print(h_j)
h_j_1 = hash_to_group(h_j,q)
r = Identity_check(h_j_1,h_j)
print(r)
'''


#AES加密


def aes_encrypt(key,plaintext):
    cipher = AES.new(key,AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(str(plaintext).encode(),AES.block_size))
    return binascii.hexlify(ciphertext).decode()
#AES解密
def aes_decrypt(key,ciphertext):
    cipher = AES.new(key,AES.MODE_ECB)
    ciphertext = binascii.unhexlify(ciphertext.encode())
    plaintext = unpad(cipher.decrypt(ciphertext),AES.block_size)
    return int(plaintext.decode())

'''
plaintext = 1234567890  # 待加密的数字
ciphertext = aes_encrypt(symmetric_key, plaintext)
print("加密后的结果：", ciphertext)
decrypted_text = aes_decrypt(symmetric_key, ciphertext)
print("解密后的结果：", decrypted_text)
'''

