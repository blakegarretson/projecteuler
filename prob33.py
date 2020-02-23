ans = []

def check(x,y,n,d):
    print(x,y,n,d)
    if x/y==n/d and n!=d:
        ans.append((n, d))

for x in range(10,100):
    n1 = x//10
    n2 = x%10
    for y in range(x,100):
        d1 = y//10
        d2 = y%10
        if d2 == 0: 
            continue #weed out trivial
        if n1 == d1:
            check(x,y,n2,d2)
        elif n1 == d2:
            check(x,y,n2,d1)
        elif n2 == d1:
            check(x,y,n1,d2)
        elif n2 == d2:
            check(x,y,n1,d1)
            
print(ans)
p=(1,1)
for x,y in ans:
    p=p[0]*x,p[1]*y
    
print(p)        
