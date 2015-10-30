import itertools

# Is this cheating?  I think this is cheating.
perms = itertools.permutations('0123456789', 10)
print(perms)

all = []
for x in perms:
    all.append("".join(x))
    
all.sort()
print(all[999999])