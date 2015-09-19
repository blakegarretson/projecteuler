# python 3

tri = []

for line in open('prob67_triangle.txt'):
    tri.append([int(x) for x in line.split()])
    
for row in tri:
    length = len(row)
    if length == 1:
        totals = row
    elif length == 2:
        totals = [x+totals[0] for x in row]
    else:
        a,b,c = row[0], row[1:-1], row[-1]
        new_totals = [a+totals[0]]
        for i in range(len(b)):
            new_totals.append(max((b[i]+totals[i], b[i]+totals[i+1])))
        new_totals.append(c+totals[-1])
        totals = new_totals[:]
        
print(max(totals))
                
        
