import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False # 소수가 아님
    return True #소수임


