import System_Params
import time


'''----------------------参数部分---------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 5


Task_data_6 = [6800,127,168,71,1960]
alpha_6 = [7132786843348027683509617106225935391508638737748699303820358533878852119799, 
            22202262115476576703143786724310994167269882708038512642473923066476527453120, 
            9846327241871927141663034382109014318524218773305585705416150605338346338779, 
            104865901099009032230511445046932151521771363669490606038609407856879688045376, 
            63388054285808307401188397777640847331427019695417334808191053678473067907114]




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
        perbed_data.append(Task_data_6[m] - alpha_6[m])
    return perbed_data

#主函数
def main():
    t = time.perf_counter()
    perb_generate(System_Params.Q)
    perbed_data = perbed_data_generate()
    print(f'cost: {time.perf_counter() - t:.8f}s')
    print(perbed_data)
main()
