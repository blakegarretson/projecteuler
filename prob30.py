#!/usr/bin/env python

combos = []
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                num = int(str(a)+str(b)+str(c)+str(d))
                numsum = a**4 + b**4 + c**4 + d**4
                if num == numsum:
                    print(num)
                    combos.append(num)
print(sum(combos))

digits = 4
maxnum = "9"*digits
#while True:
    
