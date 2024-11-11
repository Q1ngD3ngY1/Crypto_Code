import System_Param_Gen
import time





'''
------------系统参数部分------------
本次使用的是用户5
该部分包括系统参数和底层的基本函数,由System_param_Gen.py生成,包含:
****感知用户ID列表(ID可以采用简易的形式,如1,2,3,4.....)      
****感知数据列表z
****随机值信息
****哈希函数H0
****群的信息
****随机数选取,从指定的群中生成随机数,返回生成的随机数
****所有用户公钥信息
'''
#素数群q
q = 115792089237316195423570985008687907852837564279074904382605163141518161494337
#用户数量依次设置为5、6、7、8、9、10
U_ID = [1,2,3,4,5]
#任务数量依次设置为5、10、15、20、25
Task_data_9 = [6500,130,175,71,1900]

USER_NUM = 5
TASK_NUM = 5
#扰动的生成
'''
for i in range(len(alpha)):
    alpha[i] = System_Param_Gen.rand_from_primegroup(q)
print(alpha)
'''
alpha_9 = [48623361593403789316428535969317064530714456201628671361639035403693876576704, 
               80784874429251842388832045434779236362764810205959439166878424611570650297881, 
               58352991835940127247214466748328378337271782853490820375504749954439872709319, 
               10827998448947705453740509451623197092332146734030359153145444172475834481420, 
               42206922366291643865051189848072143512302276533955325280189998516140809922759]
'''
for i in range(len(beta)):
    beta[i] = System_Param_Gen.rand_from_primegroup(q)
print(beta)
'''
beta_9 = [56491329743185313365025024163899770022593081737829396913742912148448574906337,
            59490995034040151603928431097351184670106782225238471472969684750200903334072,
            15954810165928736530858278317025056892773476064894417903830115630342092396253,
            64618682483707902338863733877281433249107879768726184738131695303794939262625,
            39414674421319356654742859949810263106225945099275650286508756068131563751179]


#公钥信息
q_id_1 = (0xfdf4907810a9f5d9462a1ae09feee5ab205d32798b0ffcc379442021f84c5bbf , 0xc891eb16b0faef4bef99ba6d522fb85470a20df730808e583778aa35c7af98f5)
q_id_2 = (0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651)
q_id_3 = (0xb0915b333926d5338cadba614164c99be83592a13d8bdecb6f679593c11b79d8 , 0xb719cd4c14b89b533c60fd80bdb2b6cdb02b04baacf347ae779ac4f11adce08a)
q_id_4 = (0xc8c9d8dc87a7108ab52f17033c9527fb4c3f29f3f99625d43e97b702d782e41e , 0x4b854039ea48b60741608dbb7413cb98ed6e397036d0eeb7d8438b21c3255353)
q_id_5 = (0x582262c99657daf6c896580223061c97e32e52dea80b9302891418f37ffe9931 , 0x4bfe8f565e7d1dbfea68806b3bfd8144d9a24673237d1eaa89e89a9e15cf4cd1)
q_id_6 = (0x8d02f95bdf807897af1662dee9838a8a1730663d16f623e7f77543811e4bb7b2 , 0xdbd1672e31a7a28c0988a7c2f186ceb9fe29de8da7001ba44eb0f445646cc668)
q_id_7 = (0x6e5d57ff3248c37100246b661cc567e19db18694a851a3f9125b07282bfb8655 , 0x1d90dc7b41efaf9b9e8690508a060899b5577553b3ea024ca5e69f38ec4e1b1f)
q_id_8 = (0x6f1e62d46133e0d420a5fef03161da8638aa0a7164fbb0890627b07c8c71dfe8 , 0x5e5913a00d7740acc3a8e14ea9934ebc389db644de0e24ab5d405558df591e66)
q_id_9 = System_Param_Gen.tuple_to_point((0x13470f9d4ab33d77c579f05ee5a9eb77cf4e73d7912fc6a4d5d68ad04c45d5ff , 0xb83202ab1ba3fad8da4adf9a04d338bd87a6f359d993e8e6a007ca0f2f2453fd))

qid = [System_Param_Gen.tuple_to_point(q_id_1),
       System_Param_Gen.tuple_to_point(q_id_2),
       System_Param_Gen.tuple_to_point(q_id_3),
       System_Param_Gen.tuple_to_point(q_id_4),
       System_Param_Gen.tuple_to_point(q_id_5),
       System_Param_Gen.tuple_to_point(q_id_6),
       System_Param_Gen.tuple_to_point(q_id_7),
       System_Param_Gen.tuple_to_point(q_id_8)
       #System_Param_Gen.tuple_to_point(q_id_9),
]




#私钥信息        该py文件使用的是9
s_id_1 = System_Param_Gen.tuple_to_point((0x72e016ee64f9062d705b96f8674ca9b57a53f25e843e225a7873d4f242e8519c , 0x7a5e8f6383e433af73c82541801c2709a328c6dccb776127932da868db09f752))
s_id_2 = System_Param_Gen.tuple_to_point((0xde65c27eb50cbc1b27d12ea484530654d5cad5693f8b5d4807cd55ec8126ab1e , 0xac4b9c21e7f3bc73365e73353e01088802d886d2647350ffe4f328648f68285d))
s_id_3 = System_Param_Gen.tuple_to_point((0x73556bd165c0551f253dd68624c2985b029d94e776540aa3ec7d4ef283154d2a , 0xf6fce3e954b91d2c49b2db7104239b4232b83d2adf66495ce4b75aced8bb5bde))
s_id_4 = System_Param_Gen.tuple_to_point((0xe1a77f0d813b9650bc7a441dad6effc481132c30b6bac5e6ce4eaaa65bb50e84 , 0x588dd29297b95132c77cae7e59a8314fb565c9c18d7f2246794f744feb8fb59b))
s_id_5 = System_Param_Gen.tuple_to_point((0xb87494bb3acfcc076019d4e3e0fcbe14a4729443a65b70a10966ad7aeb8ec2cf , 0x5424248f13e0f2de6c04d0df7adb0e5072683dcfcc308a7ff65400217c21f9db))
s_id_6 = System_Param_Gen.tuple_to_point((0xf067041c8edb9183996566b0a29969a5c4564aa7b432c677c6538c927fda4b3 , 0x3d8f955647aaeb228c5e102082e608e2191473b5646fbe5dffbfaa18b4d4c2c8))
s_id_7 = System_Param_Gen.tuple_to_point((0xad47f029620b2dacd6eec09407078c93d9bda2da334aebadd715218e29bd5393 , 0x9d2c873f6cb802e148af4c1368dee6050e23e6c13777aeff36cba6911d78ff9c))
s_id_8 = System_Param_Gen.tuple_to_point((0x891fc49e91768c1ffc1b51d8da17570349e7a292d3d75735eb314f8c3eb6e049 , 0x4fbbb5614b4c9c965c67b3d3b3478976fad6b2045a16c7bf682006f6f3e6a588))
s_id_9 = System_Param_Gen.tuple_to_point((0x190b51d76ee7010acd2b1e01219bef93cee289701973fc7d7600aaf3cd751771 , 0x76bdf19c83ef5ab639a632e1ca7ddfff168cfdbe99e09fab6504b860cad6f54a))

#print(s_id_5,type(s_id_5))

'''
------------函数实现部分------------
该部分是感知用户端的主体部分,主要包括以下两个函数:
****扰动数据生成函数
****环签名生成函数
'''

#扰动数据生成函数
def perb_data_gen():
    M_51 = [Task_data_9[0]*beta_9[0],Task_data_9[1]*beta_9[1],Task_data_9[2]*beta_9[2],Task_data_9[3]*beta_9[3],Task_data_9[4]*beta_9[4]]           #乘法扰动结果
    M_52 = [Task_data_9[0]+alpha_9[0],Task_data_9[1]+alpha_9[1],Task_data_9[2]+alpha_9[2],Task_data_9[3]+alpha_9[3],Task_data_9[4]+alpha_9[4]]      #加法扰动结果

    spli_1 = str(M_51) + str(alpha_9)
    T_51 = System_Param_Gen.hash_to_prime_group(spli_1,q)

    spli_2 = str(M_52) + str(beta_9)
    T_52 = System_Param_Gen.hash_to_prime_group(spli_2,q)
    #print(M_51,M_52,T_51,T_52)

    return M_51,M_52,T_51,T_52
#perb_data_gen()

#环签名生成函数
def ring_signature_gen(T_91,T_92):
    U_9 = []                    #U_ki的集合,最后返回
    h_9 = []                    #h_ki的集合,类型应为素数群上的元素

    for i in range(len(qid)):                                   #环签名生成主体
        U_9i = System_Param_Gen.randpoint_from_ECC()            #U_1里面的元素的类型均为class 'ecpy.curves.Point'
        U_9.append(U_9i)                                      #将第i个用户的U添加到列表中
    
        spli = str(T_91) + str(T_92) + str(U_ID) + str(U_9i)
        h_9i = System_Param_Gen.hash_to_prime_group(spli,q)
        h_9.append(h_9i)

    r_9 = System_Param_Gen.rand_from_primegroup(q)
    U_99 = r_9 * q_id_9 - ((U_9[0]+h_9[0] * qid[0]) + (U_9[1]+h_9[1] * qid[1]) + (U_9[2]+h_9[2] * qid[2]) + (U_9[3]+h_9[3] * qid[3])+ (U_9[4]+h_9[4] * qid[4])
                           + (U_9[5]+h_9[5] * qid[5])+ (U_9[6]+h_9[6] * qid[6])+ (U_9[7]+h_9[7] * qid[7]))
    U_9.insert(8,U_99)

    temp_s = str(T_91) + str(T_92) + str(U_ID) + str(U_99)
    h_99 = System_Param_Gen.hash_to_prime_group(temp_s,q)
    V_9 = (h_99 + r_9) *  s_id_9

    return U_9,V_9

#_,_,T_11,T_12 = perb_data_gen()
#U_11,U_12,U_13,U_14,U_15,V_1= ring_signature_gen(T_11,T_12)
#print(U_11,U_12,U_13,U_14,U_15,V_1)


'''主函数'''
def main():
    #t = time.perf_counter()
    M_91,M_92,T_91,T_92 = perb_data_gen()
    U_9,V_9 = ring_signature_gen(T_91,T_92)
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    #print('M91:\n',M_91,'\nM_92:\n',M_92,'\n')
    #print('ring signature: \n',U_9[0],U_9[1],U_9[2],U_9[3],U_9[4],U_9[5],U_9[6],U_9[7],U_9[8],U_9[9],'\n',V_9)
    return M_91,M_92,U_9,V_9
#main()

