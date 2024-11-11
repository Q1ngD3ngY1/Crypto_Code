import paillier_variant
import System_Params
import time




'''参数或数据'''
#AES加密的对称密钥
symmetric_key = 'woshililinhahaha'.encode()
#群阶
q = 115792089237316195423570985008687907852837564279074904382605163141518161494337


#用户列表
U_ID = [1,2,3,4,5,6,7,8,9,10]
#任务列表
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 25

#数据
Task_data_3 = [4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000,
               4000,125,174,76,2000]
#Task_data_3 = (10000,130,176,70,3000)

#扰动
alpha_3 = [22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16,
           22,68,43,10,16]
#alpha_3 = [63,24,11,37,14]
'''
alpha_3 = [63522566125187066556456764927373909912726211284218421011246448508692892883960, 
           2409208470116330926832310305110493054977239499386296942801684715449791849710, 
           113517673626352500141239206018899500102813717310384125436766574738317857361980, 
           37375605603684302646951325006261092494073445795806255322644516033219539977589, 
           114880691687877779925881942767867221717253840071213558427380246744809174197327]
'''
#paillier加密的公钥
paillier_public_key = paillier_variant.public_key





'''函数部分'''

#扰动数据生成
def perb_data_gen():
    perb_data_3 = []
    for m in range(TASK_NUM):
        perb_data_3.append(Task_data_3[m] - alpha_3[m])
    return perb_data_3
'''[9937, 106, 165, 33, 2986]
perb_1 = perb_data_gen()
print(perb_1)
'''

#paillier加密任务数据函数
def pai_encrypt_data():
    encrypted_data = []
    pai = paillier_variant.Paillier()
    for m in range(TASK_NUM):
        encrypted_data.append(pai.encipher(Task_data_3[m],paillier_public_key[0],paillier_public_key[1]))
    return encrypted_data
'''
t = time.perf_counter()
en_d = pai_encrypt_data()
print(f'cost: {time.perf_counter() - t:.8f}s')
print(en_d)
'''

#paillier加密扰动的函数
def pai_encrypt_perb():
    encrypted_perbed = []
    pai = paillier_variant.Paillier()
    for m in range(TASK_NUM):
        encrypted_perbed.append(pai.encipher(alpha_3[m],paillier_public_key[0],paillier_public_key[1]))
    return encrypted_perbed
'''
t = time.perf_counter()
en_d = pai_encrypt_perb()
print(f'cost: {time.perf_counter() - t:.8f}s')
print(en_d)
'''

#paillier加密扰动的平方和函数
def pai_encrypt_perbpowsum():
    perb_pow_sum = 0
    for m in range(TASK_NUM):
        perb_pow_sum += alpha_3[m] ** 2
    pai = paillier_variant.Paillier()
    return perb_pow_sum,pai.encipher(perb_pow_sum,paillier_public_key[0],paillier_public_key[1])
'''
t = time.perf_counter()
perb_sum,en = pai_encrypt_perbpowsum()
print(f'cost: {time.perf_counter() - t:.8f}s')
print(perb_sum)
print(en)
'''
#身份认证信息生成函数
def Identity_hash(ID):
    H_j = System_Params.hash_to_group(ID,q)
    return H_j
'''
H_j = Identity_hash()
H_j_1 = System_Params.hash_to_group(H_1j,q)
'''
H_3j_1 = System_Params.hash_to_group(Identity_hash(U_ID[2]),q)



#主函数
def main():
    
    t = time.perf_counter()
    
    #生成身份验证的哈希
    H_3j = Identity_hash(U_ID[2])

    #用AES加密扰动后的数据
    perbed_data = perb_data_gen()           #生成扰动后的数据
    aes_enc_perbed_data = []                #用于存储AES加密的扰动后的数据
    for m in range(TASK_NUM):
        aes_enc_perbed_data.append(System_Params.aes_encrypt(symmetric_key,perbed_data[m]))
    
    #用AES加密: paillier同态加密后的感知数据
    pai_enc_task_data = pai_encrypt_data()  #存储paillier加密的原始感知数据
    aes_enc_pai_enc_task_data = []              #用于存储AES加密的paillier加密后的感知数据的密文
    for m in range(TASK_NUM):
        aes_enc_pai_enc_task_data.append(System_Params.aes_encrypt(symmetric_key,pai_enc_task_data[m]))
    '''测试
    pai = paillier_variant.Paillier()
    aes_de = System_Params.aes_decrypt(symmetric_key,aes_enc_pai_task_data[4])
    print(pai.decipher(aes_de,System_Params.paillier_public_key[0],System_Params.paillier_private_key[0],System_Params.paillier_private_key[1]))
    '''

    #用AES加密: paillier同态加密后的扰动alpha
    pai_enc_perb = pai_encrypt_perb()       #存储paillier加密后的扰动alpha
    aes_enc_pai_enc_perb = []                   #用于存储AES加密paillier加密后的扰动alpha
    for m in range(TASK_NUM):
        aes_enc_pai_enc_perb.append(System_Params.aes_encrypt(symmetric_key,pai_enc_perb[m]))
    '''
    pai = paillier_variant.Paillier()
    aes_de = System_Params.aes_decrypt(symmetric_key,aes_pai_enc_perb[0])
    #print(pai_enc_perb[0])
    print(type(aes_de))
    print(pai.decipher(aes_de,System_Params.paillier_public_key[0],System_Params.paillier_private_key[0],System_Params.paillier_private_key[1]))
    '''

    #用AES加密: paillier同态加密后的扰动的平方和
    _,pai_enc_perb_pow_sum = pai_encrypt_perbpowsum() #存储paillier加密后的扰动的平方和
    aes_enc_pai_enc_perbpowsum = System_Params.aes_encrypt(symmetric_key,pai_enc_perb_pow_sum)
    '''
    de = System_Params.aes_decrypt(symmetric_key,aes_pai_enc_perbpowsum)
    pai = paillier_variant.Paillier()
    print(pai.decipher(de,System_Params.paillier_public_key[0],System_Params.paillier_private_key[0],System_Params.paillier_private_key[1]))
    '''

    #计算MAC
    z_3 = 1234567890
    s = str(aes_enc_perbed_data) + str(aes_enc_pai_enc_task_data) + str(aes_enc_pai_enc_perb) + str(aes_enc_pai_enc_perbpowsum) + str(H_3j)
    mac = System_Params.MAC(s,z_3)
    
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    '''
    print(f'AES encrypt perbed data:\n')
    print(aes_enc_perbed_data,'\n')

    print(f'AES encrypt encrypted original data by paillier:\n')
    print(aes_enc_pai_enc_task_data,'\n')

    print(f'AES encrypt encrypted perb by paillier:\n')
    print(aes_enc_pai_enc_perb,'\n')
    
    print(f'AES encrypt encrypted sum of squares of perb by paillier:\n')
    print(aes_enc_pai_enc_perbpowsum,'\n')

    print(f'Identity: \n')
    print(H_3j)

    print(f'MAC: \n')
    print(mac)
    '''
    return aes_enc_perbed_data,aes_enc_pai_enc_task_data,aes_enc_pai_enc_perb,aes_enc_pai_enc_perbpowsum,H_3j,mac
#main()