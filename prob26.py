d=1
digits=[]
while d < 1000:
    digits.append((d,str(1.0/d)[2:]))
    d+=1
 
ld=0
l=0

for d,n in digits:
    f=n[0]
    sl=f
    for x in n[1:]:
        sl+=sl
        if x==f:
            if len(sl)>l:
                ld=d
                l=len(sl)
                
print(ld,l)
        
        