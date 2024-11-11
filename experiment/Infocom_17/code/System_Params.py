import pickle
import random
import time
from phe import paillier






'''--------------------------------------参数部分----------------------------------------'''
#素数选取的范围
Q = 115792089237316195423570985008687907852837564279074904382605163141518161494337

#A和B的公私钥
with open('F:\研究生论文资料\Code-用户任务扩充版本\experiment\Infocom_17\public_key_A.txt', 'rb') as file:
    pub_A = file.read()
with open('F:\研究生论文资料\Code-用户任务扩充版本\experiment\Infocom_17\private_key_A.txt', 'rb') as file:
    pri_A = file.read()
public_key_A = pickle.loads(pub_A)
private_key_A = pickle.loads(pri_A)

with open('F:\研究生论文资料\Code-用户任务扩充版本\experiment\Infocom_17\public_key_B.txt', 'rb') as file:
    pub_B = file.read()
with open('F:\研究生论文资料\Code-用户任务扩充版本\experiment\Infocom_17\private_key_B.txt', 'rb') as file:
    pri_B = file.read()
public_key_B = pickle.loads(pub_B)
private_key_B = pickle.loads(pri_B)




'''--------------------------------------函数部分-------------------------------------------'''
#选取随机数
def rand_from_group(q):
    number = random.randint(1,q-1)
    return number

#paillier加密函数
def Paillier_Encrypt(public_key,plaintext):
    ciphertext = public_key.encrypt(plaintext)
    return ciphertext

#paillier解密函数
def Paillier_Decrypt(private_key,ciphertext):
    plaintext = private_key.decrypt(ciphertext)
    return plaintext

#同态加
def homomorphic_add(ciphertext_1,ciphertext_2):
    ciphertext = ciphertext_1 + ciphertext_2
    return ciphertext



#密态指数运算
def cipher_exp(ciphertext,scalar):
    return ciphertext * scalar

'''
c1 = Paillier_Encrypt(public_key_A,12345)
c2 = Paillier_Encrypt(public_key_A,67890)

t1 = time.perf_counter()
homomorphic_add(c1,c2)
print(f'cost1: {time.perf_counter() - t1:.8f}s')

t2 = time.perf_counter()
cipher_exp(c1,43139019699327115711617780202783040092862808628341895782744823069479854552953)
print(f'cost2: {time.perf_counter() - t2:.8f}s')
'''