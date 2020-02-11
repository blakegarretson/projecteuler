import sys
nums = range(1,997)

for x in nums:
    for y in nums:
        for z in nums:
            if (x+y+z == 1000):
                l = [x,y,z]
                l.sort()
                a,b,c = l
                if a**2 + b**2 == c**2:
                    print(a,b,c)
                    print(a*b*c)
                    sys.exit()
                    
                    
