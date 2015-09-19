n = 1

longest_chain = 1
longest_chain_starting_num = 1

while n < 1000001:
#while n < 14:
    x = [n]
    while x[-1] != 1:
        if x[-1] % 2 == 0:
            x.append(x[-1]/2)
        else:
            x.append(3*x[-1]+1)
    if len(x) > longest_chain:
        longest_chain = len(x)
        longest_chain_starting_num = n
    n += 1
print "Longest chain %s from starting number %s" % (longest_chain, longest_chain_starting_num)