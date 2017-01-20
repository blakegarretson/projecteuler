n = 1
last_num = 0
num = 1
while len(str(num)) < 1000:
    num, last_num = num + last_num, num
    n += 1
    
print(n, num)