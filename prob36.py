result = []
for x in range(1,1000001):
    decstr = str(x)
    binstr = f"{x:b}"
    rdecstr = decstr[::-1]
    rbinstr = binstr[::-1]
    if decstr == rdecstr and binstr == rbinstr:
        result.append(x)
print(sum(result))

