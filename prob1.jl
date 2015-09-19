total = 0
for x in 1:999
    if (x % 3 == 0) || (x % 5 ==0) 
        total += x
    end
end
println(total)