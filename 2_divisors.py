import re
import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            large_divisors.append(i)
    return large_divisors

print(list(divisorGenerator(8)))