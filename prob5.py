divisors = range(1, 21)

n = 1
while True:
    passed = True
    for x in divisors:
        if n % x != 0:
            passed = False
            break
    if passed:
        print n
        break
    n += 1