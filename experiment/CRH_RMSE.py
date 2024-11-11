import math
import numpy as np
import gmpy2 as gy


user_data = [[4000,125,174,76,2000],
             [4871,123,180,80,1738],
             [10000,130,176,70,3000],
             [7000,120,170,50,1500],
             [7190,127,190,75,1500],

             [6800,127,168,71,1960],
             [6765,123,177,73,1955],
             [7000,120,188,70,1899],
             [6500,130,175,71,1900],
             [6610,125,176,74,1950]]
task_data =[[4000, 4871, 10000, 7000, 7190, 6800, 6765, 7000, 6500, 6610], 
            [125, 123, 130, 120, 127, 127, 123, 120, 130, 125], 
            [174, 180, 176, 170, 190, 168, 177, 188, 175, 176], 
            [76, 80, 70, 50, 75, 71, 73, 70, 71, 74], 
            [2000, 1738, 3000, 1500, 1500, 1960, 1955, 1899, 1900, 1950]]
'''
for m in range(5):
    sub = []
    for k in range(10):
        sub.append(user_data[k][m])
    task_data.append(sub)
print(task_data)
'''

X_star = [5500,125,175,65,2000]
Ground_truth = [6610,125,175,70,1946]
USER_NUM = 10
TASK_NUM = 5

#真值更新函数
def truth_update(data,weight):
    weight_sum = 0
    for k in range(USER_NUM):
        weight_sum += weight[k]
    weighted_data = 0
    for k in range(USER_NUM):
        weighted_data += weight[k] * data[k]
    truth = gy.mpfr(weighted_data / weight_sum)
    return truth

#权值更新
def weight_update(truth_start):
    dist = []
    for k in range(USER_NUM):
        usr_dist = 0
        for m in range(TASK_NUM):
            usr_dist += (user_data[k][m] - truth_start[m]) ** 2
        dist.append(usr_dist)
    dist_sum = 0
    for k in range(USER_NUM):
        dist_sum += dist[k]
    
    weight = []
    for k in range(USER_NUM):
        weight.append(gy.mpfr(math.log2(dist_sum / dist[k])))
    return weight



#计算RMSE
def RMSE(pred,truth):
    y_pred = np.array(pred)
    y_truth = np.array(truth)
    squared_error = (y_pred - y_truth) ** 2
    rmse = np.sqrt(np.mean(squared_error))
    print(rmse/100)
    return rmse/100

#主函数
def main():
    weight = [4.053828210337023, 6.329959808676942, 0.8144370371880749, 3.901744653175525, 3.588574355119819, 4.465367067921497, 4.54366733727989, 4.047240576591407, 5.209389012376964, 4.91969192118492]
    updated_truth = []
    updated_weight = weight
    for i in range(50):
        truth = []
        for m in range(TASK_NUM):
            truth.append(truth_update(task_data[m],updated_weight))
        updated_truth = truth
        updated_weight = weight_update(updated_truth)
        print("%d interation truth:"%(i+1),updated_truth)
        print("%d interation weight:"%(i+1),updated_weight)
    print(updated_truth)
    print(updated_weight)
    return updated_truth
updated_truth = main()
ut = [int(i) for i in updated_truth]
RMSE(ut,Ground_truth)
