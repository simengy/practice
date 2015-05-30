def streetRobber(street, addr):
    
    if len(street) <= addr:
        return 0

    max = 0
    for i in xrange(addr, len(street)):

        money = streetRobber(street, i + 2)    
        money += street[i]

        if max < money:
           max = money


    return max

street = [1,2,4,2,1,5,6]
print sum(street)
print streetRobber(street, 0)



