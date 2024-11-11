import System_Params
import time


'''----------------------参数部分---------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 5


Task_data_7 = [6765,123,177,73,1955]
alpha_7 = [65409304011354047237186567709588712533172325026467698363593724213142926988343, 
             112842395804061866533073652196090434308350830110184467533442888048301276525193, 
             22167638407458087456909011333524897573126473603610239756816857648794079344169, 
             44328431963488937666383030730779073358015421103939273396866799542612616315874, 
             104562966334847411476092532616950370438425171227329215456075892387002477874973]



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
        perbed_data.append(Task_data_7[m] - alpha_7[m])
    return perbed_data

#主函数
def main():
    t = time.perf_counter()
    perb_generate(System_Params.Q)
    perbed_data = perbed_data_generate()
    print(f'cost: {time.perf_counter() - t:.8f}s')
    print(perbed_data)
main()
