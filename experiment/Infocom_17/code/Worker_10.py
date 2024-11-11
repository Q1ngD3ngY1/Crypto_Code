import System_Params
import time


'''----------------------参数部分---------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 5


Task_data_10 = [6610,125,176,74,1950]
alpha_10 = [55938223678457320586225977217529546577844133102439334408923560983580220520083, 
                2848921631326935200510353395593829839243358619998526618662089992347765320249, 
                59698045928224943307611385018635183240445175697043564943040187109900517325414, 
                101453691664314943360165983077445994137973893060623835039764909777617875232048, 
                58318025073374684892780175626710443450628931464012007176340940024729693377047]



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
        perbed_data.append(Task_data_10[m] - alpha_10[m])
    return perbed_data

#主函数
def main():
    t = time.perf_counter()
    perb_generate(System_Params.Q)
    perbed_data = perbed_data_generate()
    print(f'cost: {time.perf_counter() - t:.8f}s')
    print(perbed_data)
main()
