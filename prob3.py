import math
#n = 13195
n = 600851475143

factors = []
x = 2

limit = int(math.sqrt(n))

while x < limit:
    if n % x == 0:
        factors.append(x)
    x += 1

primefactors = []
for x in factors:
    prime = True
    for y in factors:
        if x == y: continue
        if x % y == 0:
            prime = False
            break
    if prime:
        primefactors.append(x)
        
print primefactors
