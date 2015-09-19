t = 1 # triangle number order, e.g. t=7 is 7th triangle number or 1+2+3+4+5+6+7=28
divisors = []

while len(divisors) <= 500:
    n = sum(range(1,t+1)) # Generate triangle number
    
    step = 2 if n%2 else 1
    divisors = reduce(list.__add__, ([i, n//i] for i in range(1, int((n**0.5))+1, step) if n % i == 0))
#    divisors = set(reduce(list.__add__, ([i, n//i] for i in range(1, int((n**0.5))+1, step) if n % i == 0)))
    t += 1    
    
print n