allnums = range(100, 1000)

palindromes = []
        
for a in allnums:
    for b in allnums:
        x = a*b
        s = str(x)
        if s == s[::-1]:
            palindromes.append(x)
            #print "%s x %s = %s" % (a,b,x)

palindromes.sort()
print palindromes[-1]