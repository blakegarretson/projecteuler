#!/usr/bin/env python

# combos = []
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             for d in range(0,10):
#                 num = int(str(a)+str(b)+str(c)+str(d))
#                 numsum = a**4 + b**4 + c**4 + d**4
#                 if num == numsum:
#                     print(num)
#                     combos.append(num)
# print(sum(combos))

combos = []
numdigits = 5
maxnum = int("9"*(numdigits+1))
minnum = 2
num = minnum

while num <= maxnum:
    digits = [int(i) for i in list(str(num))]
    fourthed = sum([i**numdigits for i in digits])
    if fourthed == num:
        print(num)
        combos.append(num)
    num += 1

print(sum(combos))