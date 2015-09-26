
a,b = 1,1
total = 0

while b < 4000000
    x = a+b
    if x % 2 == 0
        total += x
    end
    a,b = b,x
end
println(total)