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
Task_data_6 = [6800,127,168,71,1960]

USER_NUM = 5
TASK_NUM = 5
#扰动的生成
'''
for i in range(len(alpha)):
    alpha[i] = System_Param_Gen.rand_from_primegroup(q)
print(alpha)
'''
alpha_6 = [7132786843348027683509617106225935391508638737748699303820358533878852119799, 
            22202262115476576703143786724310994167269882708038512642473923066476527453120, 
            9846327241871927141663034382109014318524218773305585705416150605338346338779, 
            104865901099009032230511445046932151521771363669490606038609407856879688045376, 
            63388054285808307401188397777640847331427019695417334808191053678473067907114]
'''
for i in range(len(beta)):
    beta[i] = System_Param_Gen.rand_from_primegroup(q)
print(beta)
'''
beta_6 = [96321293975927783042755880974012365462486511548389427413880533021415785828647,
           32295264156250754037379539127125596355229423196840927830020996252215304451424,
           104015976305374213487156936919558085635847423616431487509371110860196453355119,
           1927848903312200124407224393725963287283279889021393722717635832214325351570,
           112407580592866959566413877103054288208524060571745656063992838439106767322136]


#公钥信息
q_id_1 = (0xfdf4907810a9f5d9462a1ae09feee5ab205d32798b0ffcc379442021f84c5bbf , 0xc891eb16b0faef4bef99ba6d522fb85470a20df730808e583778aa35c7af98f5)
q_id_2 = (0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651)
q_id_3 = (0xb0915b333926d5338cadba614164c99be83592a13d8bdecb6f679593c11b79d8 , 0xb719cd4c14b89b533c60fd80bdb2b6cdb02b04baacf347ae779ac4f11adce08a)
q_id_4 = (0xc8c9d8dc87a7108ab52f17033c9527fb4c3f29f3f99625d43e97b702d782e41e , 0x4b854039ea48b60741608dbb7413cb98ed6e397036d0eeb7d8438b21c3255353)
q_id_5 = (0x582262c99657daf6c896580223061c97e32e52dea80b9302891418f37ffe9931 , 0x4bfe8f565e7d1dbfea68806b3bfd8144d9a24673237d1eaa89e89a9e15cf4cd1)
q_id_6 = System_Param_Gen.tuple_to_point((0x8d02f95bdf807897af1662dee9838a8a1730663d16f623e7f77543811e4bb7b2 , 0xdbd1672e31a7a28c0988a7c2f186ceb9fe29de8da7001ba44eb0f445646cc668))




qid = [System_Param_Gen.tuple_to_point(q_id_1),
       System_Param_Gen.tuple_to_point(q_id_2),
       System_Param_Gen.tuple_to_point(q_id_3),
       System_Param_Gen.tuple_to_point(q_id_4),
       System_Param_Gen.tuple_to_point(q_id_5),
       #System_Param_Gen.tuple_to_point(q_id_6),
    ]




#私钥信息        该py文件使用的是6
s_id_1 = System_Param_Gen.tuple_to_point((0x72e016ee64f9062d705b96f8674ca9b57a53f25e843e225a7873d4f242e8519c , 0x7a5e8f6383e433af73c82541801c2709a328c6dccb776127932da868db09f752))
s_id_2 = System_Param_Gen.tuple_to_point((0xde65c27eb50cbc1b27d12ea484530654d5cad5693f8b5d4807cd55ec8126ab1e , 0xac4b9c21e7f3bc73365e73353e01088802d886d2647350ffe4f328648f68285d))
s_id_3 = System_Param_Gen.tuple_to_point((0x73556bd165c0551f253dd68624c2985b029d94e776540aa3ec7d4ef283154d2a , 0xf6fce3e954b91d2c49b2db7104239b4232b83d2adf66495ce4b75aced8bb5bde))
s_id_4 = System_Param_Gen.tuple_to_point((0xe1a77f0d813b9650bc7a441dad6effc481132c30b6bac5e6ce4eaaa65bb50e84 , 0x588dd29297b95132c77cae7e59a8314fb565c9c18d7f2246794f744feb8fb59b))
s_id_5 = System_Param_Gen.tuple_to_point((0xb87494bb3acfcc076019d4e3e0fcbe14a4729443a65b70a10966ad7aeb8ec2cf , 0x5424248f13e0f2de6c04d0df7adb0e5072683dcfcc308a7ff65400217c21f9db))
s_id_6 = System_Param_Gen.tuple_to_point((0xf067041c8edb9183996566b0a29969a5c4564aa7b432c677c6538c927fda4b3 , 0x3d8f955647aaeb228c5e102082e608e2191473b5646fbe5dffbfaa18b4d4c2c8))




#print(s_id_5,type(s_id_5))

'''
------------函数实现部分------------
该部分是感知用户端的主体部分,主要包括以下两个函数:
****扰动数据生成函数
****环签名生成函数
'''

#扰动数据生成函数
def perb_data_gen():
    M_61 = [Task_data_6[0]*beta_6[0],Task_data_6[1]*beta_6[1],Task_data_6[2]*beta_6[2],Task_data_6[3]*beta_6[3],Task_data_6[4]*beta_6[4]]           #乘法扰动结果
    M_62 = [Task_data_6[0]+alpha_6[0],Task_data_6[1]+alpha_6[1],Task_data_6[2]+alpha_6[2],Task_data_6[3]+alpha_6[3],Task_data_6[4]+alpha_6[4]]      #加法扰动结果

    spli_1 = str(M_61) + str(alpha_6)
    T_61 = System_Param_Gen.hash_to_prime_group(spli_1,q)

    spli_2 = str(M_62) + str(beta_6)
    T_62 = System_Param_Gen.hash_to_prime_group(spli_2,q)
    #print(M_51,M_52,T_51,T_52)

    return M_61,M_62,T_61,T_62
#perb_data_gen()

#环签名生成函数
def ring_signature_gen(T_61,T_62):
    U_6 = []                    #U_ki的集合,最后返回
    h_6 = []                    #h_ki的集合,类型应为素数群上的元素

    for i in range(len(qid)):                                   #环签名生成主体
        U_6i = System_Param_Gen.randpoint_from_ECC()            #U_1里面的元素的类型均为class 'ecpy.curves.Point'
        U_6.append(U_6i)                                      #将第i个用户的U添加到列表中
    
        spli = str(T_61) + str(T_62) + str(U_ID) + str(U_6i)
        h_6i = System_Param_Gen.hash_to_prime_group(spli,q)
        h_6.append(h_6i)

    r_6 = System_Param_Gen.rand_from_primegroup(q)
    
    U_66 = r_6 * q_id_6 - ((U_6[0]+h_6[0] * qid[0]) + (U_6[1]+h_6[1] * qid[1]) + (U_6[2]+h_6[2] * qid[2]) + (U_6[3]+h_6[3] * qid[3]) + (U_6[4]+h_6[4] * qid[4]))
    U_6.insert(5,U_66)

    temp_s = str(T_61) + str(T_62) + str(U_ID) + str(U_66)
    h_66 = System_Param_Gen.hash_to_prime_group(temp_s,q)
    V_6 = (h_66 + r_6) *  s_id_6

    return U_6,V_6

#_,_,T_11,T_12 = perb_data_gen()
#U_11,U_12,U_13,U_14,U_15,V_1= ring_signature_gen(T_11,T_12)
#print(U_11,U_12,U_13,U_14,U_15,V_1)


'''主函数'''
def main():
    #t = time.perf_counter()
    M_61,M_62,T_61,T_62 = perb_data_gen()
    U_6,V_6 = ring_signature_gen(T_61,T_62)
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    #print('M61:\n',M_61,'\nM_62:\n',M_62,'\n')
    #print('ring signature: \n',U_6[0],U_6[1],U_6[2],U_6[3],U_6[4],U_6[5],U_6[6],U_6[7],U_6[8],U_6[9],'\n',V_6)
    return M_61,M_62,U_6,V_6

#main()
