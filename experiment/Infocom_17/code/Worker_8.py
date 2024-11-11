import System_Params
import time


'''----------------------参数部分---------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 5


Task_data_8 = [7000,120,188,70,1899]
alpha_8 = [82311233059362826292536458877051790059863656700534136836280522182928647995503, 
              85570166055603503963241492763829970922073310076502773750400818987063390197163, 
              50581398802476747285065499181964945506412184399799615686276017128518175627321, 
              40134484064243320410604578954571590973131345465333677911899673185710823132668, 
              104545717417648121169975128314758727909304342625913470898014862589977113121163]



'''----------------------函数部分---------------------'''

#扰动的生成
def perb_generate(q):
    r = System_Params.rand_from_group(q)
    return r
'''
alpha_1 = []
for m in range(TASK_NUM):
    alpha_1.append(perb_generate(System_Params.Q))
print(alpha_1)
'''

#扰动后的数据生成
def perbed_data_generate():
    perbed_data = []
    for m in range(TASK_NUM):
        perbed_data.append(Task_data_8[m] - alpha_8[m])
    return perbed_data

#主函数
def main():
    t = time.perf_counter()
    perb_generate(System_Params.Q)
    perbed_data = perbed_data_generate()
    print(f'cost: {time.perf_counter() - t:.8f}s')
    print(perbed_data)
main()
