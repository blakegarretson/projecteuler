import euler

maxn = 1000001
primes = euler.getPrimes(2,maxn)
print(f"Primes under {maxn}: {len(primes)}")
circular_primes = {}

for n in primes:
	if n in circular_primes:
		continue
	rotations = [n]
	n_str = str(n)
	n_list = list(n_str)
	for i in range(1,len(n_str)): # runs 0 times for 1 digit, 1 time for 2 digits, 2 times for 3 digits
		n_list = [n_list.pop()] + n_list # rotate
		rotations.append(int("".join(n_list)))
	isCircular = True
	for r in rotations:
		if r not in primes:
			isCircular = False
			break
	if isCircular:
		print(rotations)
		for r in rotations:
			circular_primes[r] = None

print(sorted(circular_primes.keys()))
print(len(circular_primes))
