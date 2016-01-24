import math

primenum = 1
n=1
while primenum <= 10001:
    n += 1
    isprime = True
    for x in range(2,int(math.sqrt(n))+1) :
        if n % x == 0:
            isprime = False
            break
    if isprime:
        primenum += 1
    
print(n)