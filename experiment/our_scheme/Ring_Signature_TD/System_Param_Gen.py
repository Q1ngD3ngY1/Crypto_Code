'''
------------模块说明------------
该py文件主要负责利用已有的公共信息,生成各方所需的系统参数，然后生成的系统参数直接由其它模块复制，一些底层公用函数
由该模块导入到其他模块中
不需要考虑该部分的时间效率问题

'''
import hashlib
import random
import time

from ecpy.curves import Curve,Point
from sympy import isprime, mod_inverse



'''
------------公共信息部分------------
****感知用户ID列表(ID可以采用简易的形式)

'''
#用户数量我们设置为5、6、7、8、9、10
U_ID = (1,2,3,4,5)              #用户ID列表



'''
------------系统参数生成函数部分------------
该部分主要包括以下函数：
****阶为素数q的循环加法群(椭圆曲线群)和循环乘法群的选取,返回素数q、循环加法群和循环乘法群       √
****双线性映射函数,返回映射结果
****任意比特串映射到椭圆曲线群的哈希函数H                                                   √                                                   
****任意比特串映射到素数群的哈希函数H0                                                     √
****主公钥的生成(包含TA的私钥),返回TA的公钥和私钥                                           √
****用户公私钥生成,返回用户公私钥                                                          √
****随机数选取,从指定的群中生成随机数,返回生成的随机数                                       √
'''

'''椭圆曲线群、循环乘法群的生成'''
#注意，我们使用的是secp256k1曲线，所以该曲线的生成元和阶是固定的，那么在获得了阶后，相当于循环乘法群的也就确定了即q = curve.order

'''截断函数:取十六进制指定前多少位,因为secp256k1生成元和阶太大了,会导致栈溢出'''
def truncate_hex_tuple(decimal_tuple, num_digits):
    decimal_list = []
    for value in decimal_tuple:
        hex_value = hex(value)[2:]  # 转换为16进制并去掉前缀"0x"
        truncated_value = hex_value[:num_digits]  # 截取指定16进制位
        decimal_value = int(truncated_value, 16)  # 转换为十进制
        decimal_list.append(decimal_value)
    return tuple(decimal_list)

#获取椭圆曲线的生成元和阶
def Obtain_ECC():
    curve = Curve.get_curve('secp256k1')
    gen = curve.generator
    order = curve.order
    return gen,order            #type of gen: ecpy.curves.Point

Gen,Ord= Obtain_ECC()
#Ord = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
#Ord = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
#print(type(gen))
#t = time.perf_counter()
#print(f'coast:{time.perf_counter() - t:.8f}s')
#print(Gen,Ord)
#生成元 = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798 , 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
#阶 = 115792089237316195423570985008687907852837564279074904382605163141518161494337             256bit

'''
#双线性映射运算        该模块存在问题,两种解决思路:一是把该模块的环境调试好，然后融入到系统里;二是把该模块的运行时间在linux上跑一下,然后在代码里加上这个时间。倾向于二
#该函数的输入是两个椭圆曲线上的点，输出一个素数群上的元素
def bilinear_pairing(P,Q,q):
    curve = secp256k1.lib.secp256k1_context_create(secp256k1.ALL_FLAGS)
    pairing_result = curve.pairing(P,Q)
    return pairing_result % q

gen,ord = Obtain_ECC()
P = 2 * gen
Q = 3 * gen
e = bilinear_pairing(P,Q,ord)
print('e : ',e)
'''


'''哈希函数H构造'''
def hash_to_point(message, curve):
    # 将消息哈希为一个大整数
    hash_int = int(hashlib.sha256(str(message).encode()).hexdigest(), 16)

    # 将哈希值限制在曲线的阶范围内
    hash_int_mod_order = hash_int % curve.order

    # 将哈希值乘以生成元得到椭圆曲线上的点
    point = hash_int_mod_order * curve.generator

    return point            #type: ecpy.curves.Point
#curve = Curve.get_curve('secp256k1')
#p = hash_to_point('hellsdsdoworld',curve)
#print(p,type(p))


'''哈希函数H0构造'''
def hash_to_prime_group(message,q):
    hash_int = int(hashlib.sha256(str(message).encode()).hexdigest(),16)
    hash_int_modq = hash_int % q
    return hash_int_modq

'''带密钥的哈希函数'''
def hash_with_key(message,q,key):
    hash_int = int(hashlib.sha256((str(message)+str(key)).encode()).hexdigest(),16)
    hash_int_modq = hash_int % q
    return hash_int_modq



'''随机数生成'''
def rand_from_primegroup(q):
    number = random.randint(1,q-1)
    return number



#随机点的生成
def randpoint_from_ECC():
    curve = Curve.get_curve('secp256k1')
    gen = curve.generator
    r = rand_from_primegroup(Ord)
    randpoint = r * gen

    return randpoint            #type of randpoint: ecpy.curves.Point
#p = randpoint_from_ECC()
#print(p,type(p))



'''主密钥生成函数'''
def master_key(curve):
    msk = rand_from_primegroup(Ord)
    mpk = msk * curve.generator
    #print(curve.generator)

    return msk,mpk          # type of mpk: ecpy.curves.Point
#curve = Curve.get_curve('secp256k1')
#msk,mpk = master_key(curve)
#print(msk,mpk)
#print(type(msk),type(mpk))
msk = 110170846878126819391846826547633261947154286293489187759670320522662172654068
mpk = Point(0x4f3abaaa6f79f594b9931b2fd9e07040ea65083ef4834d5133580c9489eaf54e , 0xc4b06381e6f24f780e62948eaa6dfaee2f123c11c51ebe18137b35a2996ae4e2,Curve.get_curve('secp256k1'))
#print(mpk,type(mpk))


#用户公私钥生成函数
def workers_key_generate(msk,ID,curve):
    Q_ID_k = hash_to_point(ID,curve)            # type of Q_ID_k: ecpy.curves.Point
    #print('type of Q_ID_k: ',type(Q_ID_k))
    S_ID_k = msk * Q_ID_k

    return S_ID_k,Q_ID_k                        #type: ecpy.curves.Point

#curve = Curve.get_curve('secp256k1')
#gen,ord = Obtain_ECC()
#print('gen,ord:',gen,ord)
#s_id_1,q_id_1 = workers_key_generate(msk,10,curve)
#print(s_id_1,q_id_1)
#print(type(s_id_1),type(q_id_1))

#元组类型转椭圆曲线点的类型
def tuple_to_point(tup):
    curve = Curve.get_curve('secp256k1')
    p = Point(tup[0],tup[1],curve)
    return p
#p = tuple_to_point((0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651))
#print(p,type(p))

'''
t1 = (0x9ebd374eea3befddf46bbb182e291fb719ee1b705b0b7802161038eb7da8a036 , 0xb96891c93bd45e9aadea192fa13f763e07dd92d70d6332edc27bbd82cfb63651)
t2 = Point(t1[0],t1[1],Curve.get_curve('secp256k1'))
print('type t1: ',type(t1))
print('type t2: ',type(t2))
print(2 * t1,'\n')
print(t2)
t = time.perf_counter()
print(rand_from_primegroup(Ord) * t2)
print(f'coast:{time.perf_counter() - t:.8f}s')
'''

'''
sigma_V_k = tuple_to_point((0x5dfff1adb6e896f0fba04bce1ac7b9d5da5e13b79fec25ac24ddae4528dc1279 , 0xdb6d72e8d384f8a814c47d528572feed2ff62e5c05630340b4c0f5119c973890))

#key = rand_from_primegroup(Ord)
key = 111840982590485175970296538423978196999515261624746272666052161982892433726189

#r_TA = rand_from_primegroup(Ord)
r_TA = 12403834576964716973717257225581128459979563295495374112786597784413837083434

perb_msk = r_TA * msk
r_mul_V_k = r_TA * sigma_V_k
print(perb_msk)
print(r_mul_V_k)
s = str(perb_msk) + str(r_mul_V_k)

h_k = hash_with_key(s,Ord,key)
print(h_k)
'''




