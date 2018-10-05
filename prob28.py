#!/usr/bin/env python3
# size must be odd
size = 1001

#diagonal patterns:
#l 2468
#r 4488

ltotal=1
rtotal=1

rmax=size**2
lmax=rmax-size+1

last_x = 0
x = 4
n=1
while n < rmax:
    n += x
    rtotal += n
    print(n,rtotal, x)
    if x == last_x:
        last_x = x
        x += 4
    else:
        last_x = x
y = 2
n=1
while n < lmax:
    n += y
    ltotal += n
    print(n,ltotal, y)
    y += 2

total = ltotal + rtotal - 1

print(total)