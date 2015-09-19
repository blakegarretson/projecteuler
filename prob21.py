n = 220

def d(Z):
    proper_div = []
    for i in range(1, Z):
        if Z%i==0: proper_div.append(i)
    #print(proper_div)
    return sum(proper_div)
    
#print(d(n))

sum_of_nums = 0
pairs = []
for a in range(1,10001):
    #print(a)
    b = d(a)
    if d(b) == a and b < 10001 and a != b:
        #amicable
        #print("  Pair:",a,b)
        pairs.append((a,b))
        sum_of_nums += a
print(pairs)
print(sum_of_nums)