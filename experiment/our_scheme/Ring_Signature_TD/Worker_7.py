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
Task_data_7 = [6765,123,177,73,1955]

USER_NUM = 5
TASK_NUM = 5
#扰动的生成
'''
for i in range(len(alpha)):
    alpha[i] = System_Param_Gen.rand_from_primegroup(q)
print(alpha)
'''
alpha_7 = [65409304011354047237186567709588712533172325026467698363593724213142926988343, 
             112842395804061866533073652196090434308350830110184467533442888048301276525193, 
             22167638407458087456909011333524897573126473603610239756816857648794079344169, 
             44328431963488937666383030730779073358015421103939273396866799542612616315874, 
             104562966334847411476092532616950370438425171227329215456075892387002477874973]
'''
for i in range(len(beta)):
    beta[i] = System_Param_Gen.rand_from_primegroup(q)
print(beta)
'''
beta_7 = [54286373262562556670580938703370275961482308613285556062877940790046781126521,
           20004169971914524100593854304258646114472112146779022197057521060187680087127,
           74642456514174140162419785535933875638930944488393735368715787701550273644075,
           100391023996677774450139666603654449135568499842947533250806957967766542256914,
           27888776210513250873461981894252006283077512951025007731675573997273515765317]


#公钥信息
q_id_1 = (0xfdf4907810a9f5d9462a1ae09feee5ab205d32798b0ffcc379442021f84c5bbf , 0xc891eb16b0faef4bef99ba6d522fb85470a20df730808e583778aa35c7af98f5)
q_id_2 = (0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651)
q_id_3 = (0xb0915b333926d5338cadba614164c99be83592a13d8bdecb6f679593c11b79d8 , 0xb719cd4c14b89b533c60fd80bdb2b6cdb02b04baacf347ae779ac4f11adce08a)
q_id_4 = (0xc8c9d8dc87a7108ab52f17033c9527fb4c3f29f3f99625d43e97b702d782e41e , 0x4b854039ea48b60741608dbb7413cb98ed6e397036d0eeb7d8438b21c3255353)
q_id_5 = (0x582262c99657daf6c896580223061c97e32e52dea80b9302891418f37ffe9931 , 0x4bfe8f565e7d1dbfea68806b3bfd8144d9a24673237d1eaa89e89a9e15cf4cd1)
q_id_6 = (0x8d02f95bdf807897af1662dee9838a8a1730663d16f623e7f77543811e4bb7b2 , 0xdbd1672e31a7a28c0988a7c2f186ceb9fe29de8da7001ba44eb0f445646cc668)
q_id_7 = System_Param_Gen.tuple_to_point((0x6e5d57ff3248c37100246b661cc567e19db18694a851a3f9125b07282bfb8655 , 0x1d90dc7b41efaf9b9e8690508a060899b5577553b3ea024ca5e69f38ec4e1b1f))



qid = [System_Param_Gen.tuple_to_point(q_id_1),
       System_Param_Gen.tuple_to_point(q_id_2),
       System_Param_Gen.tuple_to_point(q_id_3),
       System_Param_Gen.tuple_to_point(q_id_4),
       System_Param_Gen.tuple_to_point(q_id_5),
       System_Param_Gen.tuple_to_point(q_id_6),
       #System_Param_Gen.tuple_to_point(q_id_7),
    ]




#私钥信息        该py文件使用的是7
s_id_1 = System_Param_Gen.tuple_to_point((0x72e016ee64f9062d705b96f8674ca9b57a53f25e843e225a7873d4f242e8519c , 0x7a5e8f6383e433af73c82541801c2709a328c6dccb776127932da868db09f752))
s_id_2 = System_Param_Gen.tuple_to_point((0xde65c27eb50cbc1b27d12ea484530654d5cad5693f8b5d4807cd55ec8126ab1e , 0xac4b9c21e7f3bc73365e73353e01088802d886d2647350ffe4f328648f68285d))
s_id_3 = System_Param_Gen.tuple_to_point((0x73556bd165c0551f253dd68624c2985b029d94e776540aa3ec7d4ef283154d2a , 0xf6fce3e954b91d2c49b2db7104239b4232b83d2adf66495ce4b75aced8bb5bde))
s_id_4 = System_Param_Gen.tuple_to_point((0xe1a77f0d813b9650bc7a441dad6effc481132c30b6bac5e6ce4eaaa65bb50e84 , 0x588dd29297b95132c77cae7e59a8314fb565c9c18d7f2246794f744feb8fb59b))
s_id_5 = System_Param_Gen.tuple_to_point((0xb87494bb3acfcc076019d4e3e0fcbe14a4729443a65b70a10966ad7aeb8ec2cf , 0x5424248f13e0f2de6c04d0df7adb0e5072683dcfcc308a7ff65400217c21f9db))
s_id_6 = System_Param_Gen.tuple_to_point((0xf067041c8edb9183996566b0a29969a5c4564aa7b432c677c6538c927fda4b3 , 0x3d8f955647aaeb228c5e102082e608e2191473b5646fbe5dffbfaa18b4d4c2c8))
s_id_7 = System_Param_Gen.tuple_to_point((0xad47f029620b2dacd6eec09407078c93d9bda2da334aebadd715218e29bd5393 , 0x9d2c873f6cb802e148af4c1368dee6050e23e6c13777aeff36cba6911d78ff9c))



#print(s_id_5,type(s_id_5))

'''
------------函数实现部分------------
该部分是感知用户端的主体部分,主要包括以下两个函数:
****扰动数据生成函数
****环签名生成函数
'''

#扰动数据生成函数
def perb_data_gen():
    M_51 = [Task_data_7[0]*beta_7[0],Task_data_7[1]*beta_7[1],Task_data_7[2]*beta_7[2],Task_data_7[3]*beta_7[3],Task_data_7[4]*beta_7[4]]           #乘法扰动结果
    M_52 = [Task_data_7[0]+alpha_7[0],Task_data_7[1]+alpha_7[1],Task_data_7[2]+alpha_7[2],Task_data_7[3]+alpha_7[3],Task_data_7[4]+alpha_7[4]]      #加法扰动结果

    spli_1 = str(M_51) + str(alpha_7)
    T_51 = System_Param_Gen.hash_to_prime_group(spli_1,q)

    spli_2 = str(M_52) + str(beta_7)
    T_52 = System_Param_Gen.hash_to_prime_group(spli_2,q)
    #print(M_51,M_52,T_51,T_52)

    return M_51,M_52,T_51,T_52
#perb_data_gen()

#环签名生成函数
def ring_signature_gen(T_71,T_72):
    U_7 = []                    #U_ki的集合,最后返回
    h_7 = []                    #h_ki的集合,类型应为素数群上的元素

    for i in range(len(qid)):                                   #环签名生成主体
        U_7i = System_Param_Gen.randpoint_from_ECC()            #U_1里面的元素的类型均为class 'ecpy.curves.Point'
        U_7.append(U_7i)                                      #将第i个用户的U添加到列表中
    
        spli = str(T_71) + str(T_72) + str(U_ID) + str(U_7i)
        h_7i = System_Param_Gen.hash_to_prime_group(spli,q)
        h_7.append(h_7i)

    r_7 = System_Param_Gen.rand_from_primegroup(q)
    U_77 = r_7 * q_id_7 - ((U_7[0]+h_7[0] * qid[0]) + (U_7[1]+h_7[1] * qid[1]) + (U_7[2]+h_7[2] * qid[2]) + (U_7[3]+h_7[3] * qid[3])+ (U_7[4]+h_7[4] * qid[4])
                           + (U_7[5]+h_7[5] * qid[5]))
    U_7.insert(6,U_77)

    temp_s = str(T_71) + str(T_72) + str(U_ID) + str(U_77)
    h_77 = System_Param_Gen.hash_to_prime_group(temp_s,q)
    V_7 = (h_77 + r_7) *  s_id_7

    return U_7,V_7

#_,_,T_11,T_12 = perb_data_gen()
#U_11,U_12,U_13,U_14,U_15,V_1= ring_signature_gen(T_11,T_12)
#print(U_11,U_12,U_13,U_14,U_15,V_1)


'''主函数'''
def main():
    #t = time.perf_counter()
    M_71,M_72,T_71,T_72 = perb_data_gen()
    U_7,V_7 = ring_signature_gen(T_71,T_72)
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    #print('M71:\n',M_71,'\nM_72:\n',M_72,'\n')
    #print('ring signature: \n',U_7[0],U_7[1],U_7[2],U_7[3],U_7[4],U_7[5],U_7[6],U_7[7],U_7[8],U_7[9],'\n',V_7)
    return M_71,M_72,U_7,V_7


#main()
