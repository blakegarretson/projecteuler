#!/usr/bin/env python

a_range = range(2,101)
b_range = range(2,101)

nums = []
for a in a_range:
    for b in b_range:
        nums.append(a**b)

nums = {x:True for x in nums}.keys()
nums.sort()
print(len(nums))
