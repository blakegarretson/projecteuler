import math

primes = []

n=2
while n < 2e6:
    isprime = True
    for x in range(2,int(math.sqrt(n))+1) :
        if n % x == 0:
            isprime = False
            break
    if isprime:
        primes.append(n)
    n += 1
    
print(sum(primes))