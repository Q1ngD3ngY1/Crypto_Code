import math
import numpy as np
import time
'''
t = time.perf_counter()
p1 = 125 ** 2
print(f'cost1: {time.perf_counter() - t:.8f}s')

t2 = time.perf_counter()
p2 = pow(125,2)
print(f'cost2: {time.perf_counter() - t2:.8f}s')
'''

t = time.perf_counter()
p1 = np.log(100)
print(f'cost1: {time.perf_counter() - t:.8f}s')

t2 = time.perf_counter()
p2 = math.log(100)
print(f'cost2: {time.perf_counter() - t2:.8f}s')