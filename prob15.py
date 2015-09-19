print "Looping Method:"
diags = [1,1]
for n in range(1,41):
    newdiags = [] 
    last = 0
    for x in diags:
        newdiags.append(x+last)
        last = x
    newdiags.append(last)
    diags = newdiags[:]
    if len(diags) % 2 != 0: print len(diags)/2,":",diags[len(diags)/2]
#####################################    
    
print "Recursive Method:"    

n = 20
def diagonals(n):
    if n == 0: return []
    d = [1L]+diagonals(n-1)+[1L]
    return [d[i]+d[i+1] for i in range(0,len(d)-1)]
print diagonals(n*2-1)[(n*2-1)/2]



