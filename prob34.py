import math
ans =0
n = 10
while n < 99999:
    digits = []
    x = n
    while x != 0:
        r = x%10
        x = x//10
        digits.append(r)
    s = sum([math.factorial(i) for i in digits])
    if s == n:
        print(n)
        ans += n
    n += 1
print("Sum:",ans)
