'''
import System_Param_Gen
import time

#参数改为512位的,运行时间为57ms





'''
------------系统参数部分------------
本次使用的是用户1
该部分包括系统参数和底层的基本函数,由System_param_Gen.py生成,包含:
****感知用户ID列表(ID可以采用简易的形式,如1,2,3,4.....)      
****感知数据列表
****随机值信息
****哈希函数H0
****群的信息
****随机数选取,从指定的群中生成随机数,返回生成的随机数
****所有用户公钥信息
'''
#素数群q
q = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
#用户数量依次设置为5、6、7、8、9、10
U_ID = [1,2,3,4,5]
#任务数量依次设置为5、10、15、20、25
Task_data_1 = (4000,125,174,76,2000)
test_data = [j+1 for j in range(100)]
#print(test_data)
#扰动的生成
'''
for i in range(len(alpha)):
    alpha[i] = System_Param_Gen.rand_from_primegroup(q)
print(alpha)
'''
alpha_1 = []
for i in range(100):
    alpha_1.append(System_Param_Gen.rand_from_primegroup(q))
#print(alpha_1)
'''
for i in range(len(beta)):
    beta[i] = System_Param_Gen.rand_from_primegroup(q)
print(beta)
'''
beta_1 = []
for i in range(100):
    beta_1.append(System_Param_Gen.rand_from_primegroup(q))

#公钥信息
q_id_1 = System_Param_Gen.tuple_to_point((0xfdf4907810a9f5d9462a1ae09feee5ab205d32798b0ffcc379442021f84c5bbf , 0xc891eb16b0faef4bef99ba6d522fb85470a20df730808e583778aa35c7af98f5))
q_id_2 = (0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651)
q_id_3 = (0xb0915b333926d5338cadba614164c99be83592a13d8bdecb6f679593c11b79d8 , 0xb719cd4c14b89b533c60fd80bdb2b6cdb02b04baacf347ae779ac4f11adce08a)
q_id_4 = (0xc8c9d8dc87a7108ab52f17033c9527fb4c3f29f3f99625d43e97b702d782e41e , 0x4b854039ea48b60741608dbb7413cb98ed6e397036d0eeb7d8438b21c3255353)
q_id_5 = (0x582262c99657daf6c896580223061c97e32e52dea80b9302891418f37ffe9931 , 0x4bfe8f565e7d1dbfea68806b3bfd8144d9a24673237d1eaa89e89a9e15cf4cd1)

qid = [#(0xfdf4907810a9f5d9462a1ae09feee5ab205d32798b0ffcc379442021f84c5bbf , 0xc891eb16b0faef4bef99ba6d522fb85470a20df730808e583778aa35c7af98f5),
       System_Param_Gen.tuple_to_point(q_id_2),
       System_Param_Gen.tuple_to_point(q_id_3),
       System_Param_Gen.tuple_to_point(q_id_4),
       System_Param_Gen.tuple_to_point(q_id_5)]




#私钥信息        该py文件使用的是1
s_id_1 = System_Param_Gen.tuple_to_point((0x72e016ee64f9062d705b96f8674ca9b57a53f25e843e225a7873d4f242e8519c , 0x7a5e8f6383e433af73c82541801c2709a328c6dccb776127932da868db09f752))
s_id_2 = System_Param_Gen.tuple_to_point((0xde65c27eb50cbc1b27d12ea484530654d5cad5693f8b5d4807cd55ec8126ab1e , 0xac4b9c21e7f3bc73365e73353e01088802d886d2647350ffe4f328648f68285d))
s_id_3 = System_Param_Gen.tuple_to_point((0x73556bd165c0551f253dd68624c2985b029d94e776540aa3ec7d4ef283154d2a , 0xf6fce3e954b91d2c49b2db7104239b4232b83d2adf66495ce4b75aced8bb5bde))
s_id_4 = System_Param_Gen.tuple_to_point((0xe1a77f0d813b9650bc7a441dad6effc481132c30b6bac5e6ce4eaaa65bb50e84 , 0x588dd29297b95132c77cae7e59a8314fb565c9c18d7f2246794f744feb8fb59b))
s_id_5 = System_Param_Gen.tuple_to_point((0xb87494bb3acfcc076019d4e3e0fcbe14a4729443a65b70a10966ad7aeb8ec2cf , 0x5424248f13e0f2de6c04d0df7adb0e5072683dcfcc308a7ff65400217c21f9db))
#print(s_id_5,type(s_id_5))

'''
------------函数实现部分------------
该部分是感知用户端的主体部分,主要包括以下两个函数:
****扰动数据生成函数
****环签名生成函数
'''

#扰动数据生成函数
def perb_data_gen():
    M_11 = []
    M_12 = []
    for i in range(100):
        M_11.append(test_data[i]*beta_1[i])                    #乘法扰动结果
    for i in range(100):
        M_12.append(test_data[i]+alpha_1[i])     #加法扰动结果


    spli_1 = str(M_11) + str(alpha_1)
    T_11 = System_Param_Gen.hash_to_prime_group(spli_1,q)

    spli_2 = str(M_12) + str(beta_1)
    T_12 = System_Param_Gen.hash_to_prime_group(spli_2,q)
    #print(M_11,M_12,T_11,T_12)

    return M_11,M_12,T_11,T_12
#perb_data_gen()

#环签名生成函数
def ring_signature_gen(T_11,T_12):
    U_1 = []                    #U_ki的集合,最后返回
    h_1 = []                    #h_ki的集合,类型应为素数群上的元素

    for i in range(len(qid)):                                   #环签名生成主体
        U_1i = System_Param_Gen.randpoint_from_ECC()            #U_1里面的元素的类型均为class 'ecpy.curves.Point'
        U_1.append(U_1i)                                      #将第i个用户的U添加到列表中
    
        spli = str(T_11) + str(T_12) + str(U_ID) + str(U_1i)
        h_1i = System_Param_Gen.hash_to_prime_group(spli,q)
        h_1.append(h_1i)

    r_1 = System_Param_Gen.rand_from_primegroup(q)
    U_11 = r_1 * q_id_1 - ((U_1[0]+h_1[0] * qid[0]) + (U_1[1]+h_1[1] * qid[1]) + (U_1[2]+h_1[2] * qid[2]) + (U_1[3]+h_1[3] * qid[3]))
    U_1.insert(0,U_11)

    temp_s = str(T_11) + str(T_12) + str(U_ID) + str(U_11)
    h_11 = System_Param_Gen.hash_to_prime_group(temp_s,q)
    V_1 = (h_11 + r_1) *  s_id_1

    return U_1[0],U_1[1],U_1[2],U_1[3],U_1[4],V_1

#_,_,T_11,T_12 = perb_data_gen()
#U_11,U_12,U_13,U_14,U_15,V_1= ring_signature_gen(T_11,T_12)
#print(U_11,U_12,U_13,U_14,U_15,V_1)


#主函数
if __name__ == '__main__':
    t = time.perf_counter()
    M_11,M_12,T_11,T_12 = perb_data_gen()
    U_11,U_12,U_13,U_14,U_15,V_1 = ring_signature_gen(T_11,T_12)
    print(f'coast:{time.perf_counter() - t:.8f}s')
    print('M11:\n',M_11,'\nM_12:\n',M_12,'\n')
    print('ring signature: \n',U_11,U_12,U_13,U_14,U_15,'\n',V_1)

    
'''