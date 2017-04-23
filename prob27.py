import euler as e
import math

all=[]
for a in range(-999, 1000):
    print(a)
    for b in range(-1000, 1001):
        n = 0
        while True:
            result = n**2 + a*n + b
            if not e.isPrime(result):
                all.append((n, a, b, a*b))
                break
            n+=1
                      
all.sort()
print(all[-1])
