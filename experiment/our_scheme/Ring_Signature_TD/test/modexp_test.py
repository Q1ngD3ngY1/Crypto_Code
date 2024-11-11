import time
import random

def prime_group_exponentiation(g: int, x: int, p: int) -> int:
    """
    Compute g^x mod p for prime p.
    """
    if x == 0:
        return 1
    elif x == 1:
        return g % p
    else:
        y = prime_group_exponentiation(g, x // 2, p)
        if x % 2 == 0:
            return (y * y) % p
        else:
            return (g * y * y) % p

def rand_from_primegroup(q):
    number = random.randint(1,q-1)
    return number

#g = 2
p = 115792089237316195423570985008687907852837564279074904382605163141518161494337
x = rand_from_primegroup(p**2)
h = rand_from_primegroup(p**2)
t =time.perf_counter()
result = pow(h,x,p**2)
print(f'coast:{time.perf_counter() - t:.8f}s')
print(result)








'''
# 普通群指数运算
def regular_exponentiation():

    result = 463 ** 100

t = time.perf_counter()
regular_exponentiation()
print("普通群上的指数运算时间：")
print(f'coast:{time.perf_counter() - t:.8f}s')
'''