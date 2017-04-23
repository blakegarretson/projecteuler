import math 

def isPrime(n):
    n = abs(n)
    isprime = True
    for x in range(2, 
            int(math.sqrt(n))+1):
        if n % x == 0:
            isprime = False
            break
    return isprime