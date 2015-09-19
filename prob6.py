limit = 100

nums = range(1, limit+1)

sum_of_squares = 0

for x in nums:
    sum_of_squares += x*x

square_of_sums = sum(nums)**2

print square_of_sums - sum_of_squares