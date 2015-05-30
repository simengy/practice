def rainFall(terrain):

    start = 0
    end = 0

    vol = 0
    temp = 0

    for i in range(1, len(terrain)):
        print i, terrain[i], start, end, vol
    
        if terrain[i] < terrain[start]:
            
            temp += terrain[start] - terrain[i]

        end = i
        
        if terrain[start] <= terrain[end]:
            start = end
            vol += temp
            temp = 0

        if i == len(terrain)-1 and terrain[end] < terrain[start]:
            temp -= (terrain[start] - terrain[end]) * (end - start) 
            vol += temp

    return vol


terrain = [3,1,2,4,5,1,3]
print terrain
print rainFall(terrain)
