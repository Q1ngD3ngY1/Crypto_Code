import System_Params
import time


'''----------------------参数部分---------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 5


Task_data_9 = [6500,130,175,71,1900]
alpha_9 = [48623361593403789316428535969317064530714456201628671361639035403693876576704, 
               80784874429251842388832045434779236362764810205959439166878424611570650297881, 
               58352991835940127247214466748328378337271782853490820375504749954439872709319, 
               10827998448947705453740509451623197092332146734030359153145444172475834481420, 
               42206922366291643865051189848072143512302276533955325280189998516140809922759]



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
        perbed_data.append(Task_data_9[m] - alpha_9[m])
    return perbed_data

#主函数
def main():
    t = time.perf_counter()
    perb_generate(System_Params.Q)
    perbed_data = perbed_data_generate()
    print(f'cost: {time.perf_counter() - t:.8f}s')
    print(perbed_data)
main()
