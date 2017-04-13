import decimal
decimal.getcontext().prec=10000

longest_num=0
longest=0

n=1
while n < 1000:
    #print('working on ', n)
    digits = str(decimal.Decimal(1.0) /
            decimal.Decimal(n))[2:]
    if len(digits) > 1: 
        for x in range(2, 5001):
            if digits[x:].startswith(
                        digits[:x]):
                #print(n,x,digits)
                if x > longest:
                    longest_num = n
                    longest = x
                break
    n += 1
   
print('------------')                
print('num: ', longest_num,'\nlength: ', longest)