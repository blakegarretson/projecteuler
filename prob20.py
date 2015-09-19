def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

f = factorial(100)        
print(f)

total = 0
for digit in str(f):
    total += int(digit)
print(total)
#print(factorial(100))