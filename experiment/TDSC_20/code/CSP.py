
import math
import paillier_variant
import random
import time
import gmpy2 as gy
import pickle
import sys


'''-----------------------------------参数------------------------------------------'''
#paillier变体加密的公私钥
paillier_public_key = paillier_variant.public_key
paillier_private_key = paillier_variant.private_key

#群阶
q = 115792089237316195423570985008687907852837564279074904382605163141518161494337

#用户列表
U_ID = [1,2,3,4,5,6,7,8,9,10]
#任务列表
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 25


with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\B_sum_dist_auxi.txt","rb") as file:
    Serialized_B_sum_dist_auxi = file.read()
B_sum_dist_auxi = pickle.loads(Serialized_B_sum_dist_auxi)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\Aggre_B_C_distcon.txt","rb") as file:
    Serialized_Aggre_B_C_distcon = file.read()
Aggre_B_C_distcon = pickle.loads(Serialized_Aggre_B_C_distcon)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_b_dist_auxi.txt","rb") as file:
    Serialized_b_sum_dist_auxi = file.read()
bk_sum_dist_auxi = pickle.loads(Serialized_b_sum_dist_auxi)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_b_distcon_k.txt","rb") as file:
    Serialized_b_C_distcon_k = file.read()
bk_C_distcon_k = pickle.loads(Serialized_b_C_distcon_k)

pai = paillier_variant.Paillier()


'''---------------------------------函数部分----------------------------------------'''
#Step Q2
def weight_update():

    #计算sum_dk
    sum_dk = []
    for k in range(USER_NUM):
        tmp = pai.decipher(bk_C_distcon_k[k],paillier_public_key[0],paillier_private_key[0],paillier_private_key[1])
        sum_dk.append(bk_sum_dist_auxi[k]+tmp)

    #计算B_sum_dist
    B_sum_dist = B_sum_dist_auxi + pai.decipher(Aggre_B_C_distcon,paillier_public_key[0],paillier_private_key[0],paillier_private_key[1])
    
    #更新权值
    Bk_weight = []
    for k in range(USER_NUM):
        Bk_weight.append(int(math.log2(B_sum_dist / sum_dk[k])))

    c_k = []
    for k in range(USER_NUM):
        c_k.append(random.randint(1,200))
    ck_Bk_weight = []
    for k in range(USER_NUM):
        ck_Bk_weight.append(Bk_weight[k] + c_k[k])

    pai_enc_ck = []                                 #用paillier加密c_k
    for k in range(USER_NUM):
        pai_enc_ck.append(pai.encipher(c_k[k],paillier_public_key[0],paillier_public_key[1]))

    return Bk_weight,c_k,ck_Bk_weight,pai_enc_ck
Bk_weight,c_k,ck_Bk_weight,pai_enc_ck = weight_update()
'''
Bk_weight,c_k,ck_Bk_weight,pai_enc_ck = weight_update()
Serialized_Bk_weight = pickle.dumps(Bk_weight)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\Bk_weight.txt","wb") as file:
    file.write(Serialized_Bk_weight)
Serialized_c_k = pickle.dumps(c_k)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\c_k.txt","wb") as file:
    file.write(Serialized_c_k)
Serialized_ck_Bk_weight = pickle.dumps(ck_Bk_weight)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\ck_Bk_weight.txt","wb") as file:
    file.write(Serialized_ck_Bk_weight)
Serialized_pai_enc_ck = pickle.dumps(pai_enc_ck)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\pai_enc_ck.txt","wb") as file:
    file.write(Serialized_pai_enc_ck)
'''

#真值更新辅助函数Step Q4
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\c_k.txt","rb") as file:
    Serialized_c_k = file.read()
c_k = pickle.loads(Serialized_c_k)


with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_c_m.txt","rb") as file:
    Serialized_C_c_m = file.read()
C_c_m = pickle.loads(Serialized_C_c_m)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\C_alpha_m.txt","rb") as file:
    Serialized_C_alpha_m = file.read()
C_alpha_m = pickle.loads(Serialized_C_alpha_m)

size_ccm = 0
for m in range(TASK_NUM):
    size_ccm += sys.getsizeof(C_c_m)
size_cam = 0
for m in range(TASK_NUM):
    size_cam += sys.getsizeof(C_alpha_m)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\pai_enc_perb.txt","rb") as file:
    Serialized_pai_enc_perb = file.read()
pai_enc_perb = pickle.loads(Serialized_pai_enc_perb)

size_pep = 0
for k in range(USER_NUM):
    for m in range(TASK_NUM):
        size_pep += sys.getsizeof(pai_enc_perb[k][m])
def truth_update_auxi():
    #先解密获得各个感知用户的扰动
    perb = []
    for k in range(USER_NUM):
        sub_list = []
        for m in range(TASK_NUM):
            sub_list.append(pai.decipher(pai_enc_perb[k][m],paillier_public_key[0],paillier_private_key[0],paillier_private_key[1]))
        perb.append(sub_list)
    
    #计算sum_rand_m
    sum_rand_m = []
    for m in range(TASK_NUM):
        D_Ccm = pai.decipher(C_c_m[m],paillier_public_key[0],paillier_private_key[0],paillier_private_key[1])
        D_Cam = pai.decipher(C_alpha_m[m],paillier_public_key[0],paillier_private_key[0],paillier_private_key[1])
        #print(D_Ccm)
        #print(D_Cam)
        tmp_ca = 0
        for k in range(USER_NUM):
            tmp_ca += c_k[k] + perb[k][m]
        sum_rand_m.append(D_Ccm + tmp_ca - D_Cam)
    sum_ck = 0
    for k in range(USER_NUM):
        sum_ck += c_k[k]
    return sum_rand_m,sum_ck
sum_rand_m,sum_ck = truth_update_auxi()
size_srm = 0
for m in range(TASK_NUM):
    size_srm += sys.getsizeof(sum_rand_m[m])
'''
sum_rand_m,sum_ck = truth_update_auxi()
Serialized_sum_rand_m = pickle.dumps(sum_rand_m)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_rand_m.txt","wb") as file:
    file.write(Serialized_sum_rand_m)
Serialized_sum_ck = pickle.dumps(sum_ck)
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\TDSC_20\code\数据\sum_ck.txt","wb") as file:
    file.write(Serialized_sum_ck)
'''

#主函数
def main():
    #t = time.perf_counter()
    weight_update()
    truth_update_auxi()
    print(sys.getsizeof(B_sum_dist_auxi)+sys.getsizeof(Aggre_B_C_distcon)+sys.getsizeof(bk_sum_dist_auxi)+sys.getsizeof(bk_C_distcon_k)+
          sys.getsizeof(ck_Bk_weight)+sys.getsizeof(pai_enc_ck)+size_ccm+size_cam+size_pep+size_srm+sys.getsizeof(sum_ck))
    #print(f'cost: {time.perf_counter() - t:.8f}s')
main()

















