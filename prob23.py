def finddivisors(n):
    divisors = {}
    for i in range(1, n):
        if n%i == 0:
            divisors[i] = True
    return divisors.keys()
    
def evaluate(n):
    #print(finddivisors(n))
    nsum = sum(finddivisors(n))
    #print(n, nsum)
    if n > nsum:
        n_type = 'deficient'
    elif n < nsum:
        n_type = 'abundant'
    else:
        n_type = 'perfect'
    return n_type

# Okay, let's brute force this mofo. Elegance, shmelegance.
    
all_abundants = []

for x in range(12, 28124):
    z = evaluate(x)
    if z == 'abundant':
        all_abundants.append(x)

ints_not_sum_of_two_abundant_nums = []
for x in range(1, 28124):
    is_the_sum = False
    for y in all_abundants:
        if y > x:
            break
        z = x-y
        if z in all_abundants:
            is_the_sum = True
            break
    if is_the_sum == False:
        ints_not_sum_of_two_abundant_nums.append(x)
print(sum(ints_not_sum_of_two_abundant_nums))