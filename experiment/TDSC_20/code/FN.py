import math
import paillier_variant
import random
import System_Params
import time
import Worker_1
import Worker_2
import Worker_3
import Worker_4
import Worker_5
import Worker_6
import Worker_7
import Worker_8
import Worker_9
import Worker_10
import gmpy2 as gy
import pickle
import sys





'''----------------------------参数和数据部分--------------------------------------------'''
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

#paillier加密的公钥
paillier_public_key = paillier_variant.public_key

#用户数据部分
#t1 = time.perf_counter()
aes_enc_perbed_data_1,aes_enc_pai_enc_task_data_1,aes_enc_pai_enc_perb_1,aes_enc_pai_enc_perbpowsum_1,H_j_1,mac_1 = Worker_1.main()
aes_enc_perbed_data_2,aes_enc_pai_enc_task_data_2,aes_enc_pai_enc_perb_2,aes_enc_pai_enc_perbpowsum_2,H_j_2,mac_2 = Worker_2.main()
aes_enc_perbed_data_3,aes_enc_pai_enc_task_data_3,aes_enc_pai_enc_perb_3,aes_enc_pai_enc_perbpowsum_3,H_j_3,mac_3 = Worker_3.main()
aes_enc_perbed_data_4,aes_enc_pai_enc_task_data_4,aes_enc_pai_enc_perb_4,aes_enc_pai_enc_perbpowsum_4,H_j_4,mac_4 = Worker_4.main()
aes_enc_perbed_data_5,aes_enc_pai_enc_task_data_5,aes_enc_pai_enc_perb_5,aes_enc_pai_enc_perbpowsum_5,H_j_5,mac_5 = Worker_5.main()
'''
aes_enc_perbed_data_6,aes_enc_pai_enc_task_data_6,aes_enc_pai_enc_perb_6,aes_enc_pai_enc_perbpowsum_6,H_j_6,mac_6 = Worker_6.main()
aes_enc_perbed_data_7,aes_enc_pai_enc_task_data_7,aes_enc_pai_enc_perb_7,aes_enc_pai_enc_perbpowsum_7,H_j_7,mac_7 = Worker_7.main()
aes_enc_perbed_data_8,aes_enc_pai_enc_task_data_8,aes_enc_pai_enc_perb_8,aes_enc_pai_enc_perbpowsum_8,H_j_8,mac_8 = Worker_8.main()
aes_enc_perbed_data_9,aes_enc_pai_enc_task_data_9,aes_enc_pai_enc_perb_9,aes_enc_pai_enc_perbpowsum_9,H_j_9,mac_9 = Worker_9.main()
aes_enc_perbed_data_10,aes_enc_pai_enc_task_data_10,aes_enc_pai_enc_perb_10,aes_enc_pai_enc_perbpowsum_10,H_j_10,mac_10 = Worker_10.main()
'''
#print(f'cost1: {time.perf_counter() - t1:.8f}s')

aes_enc_perbed_data = [aes_enc_perbed_data_1,                   #二维列表,用于存储所有用户的AES加密后的扰动的数据
                       aes_enc_perbed_data_2,
                       aes_enc_perbed_data_3,
                       aes_enc_perbed_data_4,
                       aes_enc_perbed_data_5]
'''                       
                       aes_enc_perbed_data_6,
                       aes_enc_perbed_data_7,
                       aes_enc_perbed_data_8,
                       aes_enc_perbed_data_9,
                       aes_enc_perbed_data_10
'''                         
aes_enc_pai_enc_task_data = [aes_enc_pai_enc_task_data_1,       #二维列表,用于存储所有用户的AES加密后的paillier加密的原始感知数据
                             aes_enc_pai_enc_task_data_2,
                             aes_enc_pai_enc_task_data_3,
                             aes_enc_pai_enc_task_data_4,
                             aes_enc_pai_enc_task_data_5]
'''                             
                             aes_enc_pai_enc_task_data_6,
                             aes_enc_pai_enc_task_data_7,
                             aes_enc_pai_enc_task_data_8,
                             aes_enc_pai_enc_task_data_9,
                             aes_enc_pai_enc_task_data_10                    
'''                             
aes_enc_pai_enc_perb = [aes_enc_pai_enc_perb_1,                 #二维列表,用于存储所有用户的AES加密后的paillier加密的扰动
                        aes_enc_pai_enc_perb_2,
                        aes_enc_pai_enc_perb_3,
                        aes_enc_pai_enc_perb_4,
                        aes_enc_pai_enc_perb_5]
'''                        
                        aes_enc_pai_enc_perb_6,
                        aes_enc_pai_enc_perb_7,
                        aes_enc_pai_enc_perb_8,
                        aes_enc_pai_enc_perb_9,
                        aes_enc_pai_enc_perb_10
'''                           
aes_enc_pai_enc_perbpowsum = [aes_enc_pai_enc_perbpowsum_1,     #一维列表,用于存储所有用户的AES加密后的paillier加密的扰动的平方和
                              aes_enc_pai_enc_perbpowsum_2,
                              aes_enc_pai_enc_perbpowsum_3,
                              aes_enc_pai_enc_perbpowsum_4,
                              aes_enc_pai_enc_perbpowsum_5]
'''                              
                              aes_enc_pai_enc_perbpowsum_6,
                              aes_enc_pai_enc_perbpowsum_7,
                              aes_enc_pai_enc_perbpowsum_8,
                              aes_enc_pai_enc_perbpowsum_9,
                              aes_enc_pai_enc_perbpowsum_10
'''                    
H_j = [H_j_1,H_j_2,H_j_3,H_j_4,H_j_5]
       #H_j_6,H_j_7,H_j_8,H_j_9,H_j_10                          #一维列表,用于存储所有用户的身份验证信息

mac = [mac_1,mac_2,mac_3,mac_4,mac_5]
      # mac_6,mac_7,mac_8,mac_9,mac_10                           #一维列表,用于存储所有用户的消息认证码信息

z_k = [13180131810,17844599179,1234567890,12345678911,12345678912]
       #12345678913,12345677913,12345677918,12345677919,123456779110

#身份验证信息
H_j_1 = [Worker_1.H_1j_1,Worker_2.H_2j_1,Worker_3.H_3j_1,Worker_4.H_4j_1,Worker_5.H_5j_1]
         #Worker_6.H_6j_1,Worker_7.H_7j_1,Worker_8.H_8j_1,Worker_9.H_9j_1,Worker_10.H_10j_1

#初始化每个任务的真值
X_star = [3970,50,125,60,1974,3970,50,125,60,1974,3970,50,125,60,1974,3970,50,125,60,1974,3970,50,125,60,1974]
#X_star = [2500,40,125,30,1400]

#B = 81865220522310876359821923958014629473482453552683504256598581056589131611406
#b_k = [42130861376655068110503503409436748599403846380938846605487325203446551579924, 68939818965071087917339240837522460981164224612940224838126641356938398896110, 71286814059306956989906697515358610266576225553176620266040834870075009686107, 12749368644171140068734795603323589148150935550801266549502942456294820029674, 5244731935645384263583014494452441403745666892541197230589487285682909199124]
B = 100
b_k = [11,23,35,44,52]  #66,77,88,99,95]

pai = paillier_variant.Paillier()


'''----------------------------函数部分-------------------------------------------------------'''
#消息完整性检验函数
def message_integrity_check(s,zk,local_mac):
    #s = str(aes_enc_perbed_data[0]) + str(aes_enc_pai_enc_task_data[0]) + str(aes_enc_pai_enc_perb[0]) + str(aes_enc_pai_enc_perbpowsum[0]) + str(H_j[0])
    mac_p = System_Params.MAC(s,zk)
    if mac_p == local_mac:
        return 1
    else:
        return 0


#身份和数据完整性检测函数
def check():

    #验证感知用户身份
    print('Identity Verifing...')
    for k in range(USER_NUM):
        if System_Params.Identity_check(H_j_1[k],H_j[k]) == 1:
            print("%d user's identity is correct.\n"%(k+1))
        else:
            print("%d user's identity is error.\n"%(k+1))
    
    #数据完整性检测
    print("Data Integrity Checking...")
    for k in range(USER_NUM):
        s = str(aes_enc_perbed_data[k]) + str(aes_enc_pai_enc_task_data[k]) + str(aes_enc_pai_enc_perb[k]) + str(aes_enc_pai_enc_perbpowsum[k]) + str(H_j[k])
        if message_integrity_check(s,z_k[k],mac[k]) == 1:
            print("%d user's data is complete.\n"%(k+1))
        else :
            print("%d user's data is not complete.\n"%(k+1))
    

#解密AES加密的数据
def Decrypt_aes_en():
    perbed_data = []
    pai_enc_task_data = []
    pai_enc_perb = []
    pai_enc_perbpowsum = []

    #获取每个用户被扰动的数据
    for k in range(USER_NUM):
        sub_list = []
        for m in range(TASK_NUM):
            sub_list.append(System_Params.aes_decrypt(symmetric_key,aes_enc_perbed_data[k][m]))
        perbed_data.append(sub_list)
    
    #获取每个用户的paillier加密的原始感知数据
    t = time.perf_counter()
    for k in range(USER_NUM):
        sub_list = []
        for m in range(TASK_NUM):
            sub_list.append(System_Params.aes_decrypt(symmetric_key,aes_enc_pai_enc_task_data[k][m]))
        pai_enc_task_data.append(sub_list)
    print(f'cost: {time.perf_counter() - t:.8f}s')
    #获取每个用户的paillier加密的扰动
    for k in range(USER_NUM):
        sub_list = []
        for m in range(TASK_NUM):
            #t = time.perf_counter()
            sub_list.append(System_Params.aes_decrypt(symmetric_key,aes_enc_pai_enc_perb[k][m]))
            #print(f'cost: {time.perf_counter() - t:.8f}s')
        pai_enc_perb.append(sub_list)
    
    #获取每个用户的paillier加密的扰动的平方和
    
    for k in range(USER_NUM):
        pai_enc_perbpowsum.append(System_Params.aes_decrypt(symmetric_key,aes_enc_pai_enc_perbpowsum[k]))
    
    return perbed_data,pai_enc_task_data,pai_enc_perb,pai_enc_perbpowsum

perbed_data,pai_enc_task_data,pai_enc_perb,pai_enc_perbpowsum = Decrypt_aes_en()

size_pep = 0
for k in range(USER_NUM):
    for m in range(TASK_NUM):
        size_pep += sys.getsizeof(pai_enc_perb[k][m])

'''
Serialized_pai_enc_perb = pickle.dumps(pai_enc_perb)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\pai_enc_perb.txt","wb") as file:
    file.write(Serialized_pai_enc_perb)
'''


#权值更新辅助函数Step Q1
def weight_update_auxi():
    dist_auxi = []
    for k in range(USER_NUM):
        sub_list = []
        for m in range(TASK_NUM):
            sub_list.append(perbed_data[k][m] - X_star[m])
        dist_auxi.append(sub_list)
    
    #计算C_distcon_k
    C_distcon_k = []
    for k in range(USER_NUM):
        pai = paillier_variant.Paillier()
        c = 1
        for m in range(TASK_NUM):
            #t = time.perf_counter()
            c = pai.homomorphic_addition(c,pai.scalar_exponentiation(pai_enc_perb[k][m],2*dist_auxi[k][m],paillier_public_key[0]),paillier_public_key[0])
            #print(f'cost: {time.perf_counter() - t:.8f}s')
        #t = time.perf_counter()
        c = pai.homomorphic_addition(c,pai_enc_perbpowsum[k],paillier_public_key[0])
        #print(f'cost: {time.perf_counter() - t:.8f}s')
        C_distcon_k.append(c)
    
    
    Aggre_C_distcon = 1
    pai = paillier_variant.Paillier()
    for k in range(USER_NUM):
        Aggre_C_distcon = pai.homomorphic_addition(Aggre_C_distcon,C_distcon_k[k],paillier_public_key[0])
    #t = time.perf_counter()
    Aggre_B_C_distcon = pai.scalar_exponentiation(Aggre_C_distcon,B,paillier_public_key[0])             #---------------
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    B_sum_dist_auxi = 0
    for k in range(USER_NUM):
        for m in range(TASK_NUM):
            B_sum_dist_auxi += dist_auxi[k][m] ** 2
    B_sum_dist_auxi = B_sum_dist_auxi * B                                                               #---------------

    
    b_sum_dist_auxi = []                                                                                #---------------
    for k in range(USER_NUM):
        b_sum_k = 0
        for m in range(TASK_NUM):
            b_sum_k += dist_auxi[k][m] ** 2
        b_sum_dist_auxi.append(b_sum_k * b_k[k])
    b_C_distcon_k = []                                                                                  #---------------
    for k in range(USER_NUM):
        #t = time.perf_counter()
        b_C_distcon_k.append(pai.scalar_exponentiation(C_distcon_k[k],b_k[k],paillier_public_key[0]))
        #print(f'cost: {time.perf_counter() - t:.8f}s')
    return B_sum_dist_auxi,Aggre_B_C_distcon,b_sum_dist_auxi,b_C_distcon_k
B_sum_dist_auxi,Aggre_B_C_distcon,b_sum_dist_auxi,b_C_distcon_k = weight_update_auxi()
'''
B_sum_dist_auxi,Aggre_B_C_distcon,b_sum_dist_auxi,b_C_distcon_k = weight_update_auxi()
Serialized_B_sum_dist_auxi = pickle.dumps(B_sum_dist_auxi)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\B_sum_dist_auxi.txt","wb") as file:
    file.write(Serialized_B_sum_dist_auxi)
Serialized_Aggre_B_C_distcon = pickle.dumps(Aggre_B_C_distcon)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\Aggre_B_C_distcon.txt","wb") as file:
    file.write(Serialized_Aggre_B_C_distcon)
Serialized_b_sum_dist_auxi = pickle.dumps(b_sum_dist_auxi)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_b_dist_auxi.txt","wb") as file:
    file.write(Serialized_b_sum_dist_auxi)
Serialized_b_C_distcon_k = pickle.dumps(b_C_distcon_k)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_b_distcon_k.txt","wb") as file:
    file.write(Serialized_b_C_distcon_k)
'''


#真值更新预热函数Step Q3
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ck_Bk_weight.txt","rb") as file:
    Serialized_ck_Bk_weight = file.read()
ck_Bk_weight = pickle.loads(Serialized_ck_Bk_weight)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\pai_enc_ck.txt","rb") as file:
    Serialized_pai_enc_ck = file.read()
pai_enc_ck = pickle.loads(Serialized_pai_enc_ck)

def truth_update_pre():

    #计算ck_weight
    ck_weight = []
    for k in range(USER_NUM):
        ck_weight.append(ck_Bk_weight[k] - int(math.log2(B / b_k[k])))
    
    #计算WX_m
    WX_m = []
    for m in range(TASK_NUM):
        tmp_wxm = 0
        for k in range(USER_NUM):
            tmp_wxm += perbed_data[k][m] * ck_weight[k]
        WX_m.append(tmp_wxm)
    
    #计算密文C_c_m,C_alpha_m
    beta_1 = []
    beta_2 = []
    for m in range(TASK_NUM):
        beta_1.append(random.randint(1,q - 1))
        beta_2.append(random.randint(1,q - 1))
    pai_enc_beta_1 = []
    pai_enc_beta_2 = []
    for m in range(TASK_NUM):
        pai_enc_beta_1.append(pai.encipher(beta_1[m],paillier_public_key[0],paillier_public_key[1]))
        pai_enc_beta_2.append(pai.encipher(beta_2[m],paillier_public_key[0],paillier_public_key[1]))
    
    C_c_m = []
    
    for m in range(TASK_NUM):
        tmp_Ccm = 1
        for k in range(USER_NUM):
            tmp_Ccm = pai.homomorphic_addition(tmp_Ccm,pai.scalar_exponentiation(pai_enc_ck[k],perbed_data[k][m],paillier_public_key[0]),paillier_public_key[0])
        C_c_m.append(pai.homomorphic_addition(tmp_Ccm,pai_enc_beta_1[m],paillier_public_key[0]))
        
    
    C_alpha_m = []
    for m in range(TASK_NUM):
        tmp_Cam = 1
        for k in range(USER_NUM):
            tmp_Cam = pai.homomorphic_addition(tmp_Cam,pai.scalar_exponentiation(pai_enc_perb[k][m],ck_weight[k],paillier_public_key[0]),paillier_public_key[0])
        tmp_Cam = pai.homomorphic_addition(tmp_Cam,pai_enc_beta_2[m],paillier_public_key[0])
        C_alpha_m.append(tmp_Cam)
    return ck_weight,WX_m,beta_1,beta_2,C_c_m,C_alpha_m

ck_weight,WX_m,beta_1,beta_2,C_c_m,C_alpha_m = truth_update_pre()
ccm = []
for m in range(TASK_NUM):
    ccm.append(C_c_m[m])
cam = []
for m in range(TASK_NUM):
    cam.append(C_alpha_m[m])
'''
Serialized_ck_weight = pickle.dumps(ck_weight)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ck_weight.txt","wb") as file:
    file.write(Serialized_ck_weight)
Serialized_WX_m = pickle.dumps(WX_m)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\WX_m.txt","wb") as file:
    file.write(Serialized_WX_m)
Serialized_beta_1 = pickle.dumps(beta_1)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ebta_1.txt","wb") as file:
    file.write(Serialized_beta_1)
Serialized_beta_2 = pickle.dumps(beta_2)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ebta_2.txt","wb") as file:
    file.write(Serialized_beta_2)
Serialized_C_c_m = pickle.dumps(C_c_m)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_c_m.txt","wb") as file:
    file.write(Serialized_C_c_m)
Serialized_C_alpha_m = pickle.dumps(C_alpha_m)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_alpha_m.txt","wb") as file:
    file.write(Serialized_C_alpha_m)
'''


#真值更新
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ck_weight.txt","rb") as file:
    Serialized_ck_weight = file.read()
ck_weight = pickle.loads(Serialized_ck_weight)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\WX_m.txt","rb") as file:
    Serialized_WX_m = file.read()
WX_m = pickle.loads(Serialized_WX_m)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ebta_1.txt","rb") as file:
    Serialized_beta_1 = file.read()
beta_1 = pickle.loads(Serialized_beta_1)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ebta_2.txt","rb") as file:
    Serialized_beta_2 = file.read()
beta_2 = pickle.loads(Serialized_beta_2)


with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_rand_m.txt","rb") as file:
    Serialized_sum_rand_m = file.read()
sum_rand_m = pickle.loads(Serialized_sum_rand_m)
srm = []
for m in range(TASK_NUM):
    srm.append(sum_rand_m[m])
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_ck.txt","rb") as file:
    Serialized_sum_ck = file.read()
sum_ck = pickle.loads(Serialized_sum_ck)

X_up = []

def truth_update():
    #先计算ck_weight的和
    sum_ck_weight = 0
    for k in range(USER_NUM):
        sum_ck_weight += ck_weight[k]
    
    fenmu = sum_ck_weight - sum_ck
    #更新真值
    for m in range(TASK_NUM):
        fenzi = WX_m[m] - sum_rand_m[m] + beta_1[m] - beta_2[m]
        X_up.append(fenzi / fenmu)
    return X_up

#主函数
def main():
   # t= time.perf_counter()
    check()
    Decrypt_aes_en()
    weight_update_auxi()
    truth_update_pre()
    X = truth_update()
    print("Updated Truth:",X)
    print(size_pep+sys.getsizeof(B_sum_dist_auxi)+sys.getsizeof(Aggre_B_C_distcon)+sys.getsizeof(b_sum_dist_auxi)+sys.getsizeof(b_C_distcon_k)+sys.getsizeof(ck_Bk_weight)+
          sys.getsizeof(pai_enc_ck)+sys.getsizeof(ccm)+sys.getsizeof(cam)+sys.getsizeof(srm)+sys.getsizeof(sum_ck))
    #print(f'cost: {time.perf_counter() - t:.8f}s')
#main()








