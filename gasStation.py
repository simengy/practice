# O(N^2) complexity
def gasStation(tank, cost):

    N = len(tank)
    
    for i in range(N):

        if finished(tank, cost, i):
            return i

    return None

def finished(tank, cost, start):

    res = 0

    N = len(tank)

    for i in range(N):
        
        # periodic
        if i + start >= N:
            ind = start + i - N
        else:
            ind = start + i
        
        if res < 0:
            return False

        res += tank[ind]

        res -= cost[ind]

    if res >= 0: 
        return True
    else:
        return False


# O(N)
def gasStation2(tank, cost):

    if sum(tank) < sum(cost):
    
        return None

    rest = 0
    station = 0
    for i in range(len(tank)):
        
        rest += tank[i]

        if rest < cost[i]:
            station = i + 1
            rest = 0
        else:
            rest = rest - cost[i]
    
    if rest < 0:
        return None
    else:
        return station




tank = [0.2, 0.4, 0.6, 0.3]
cost = [0.3, 0.1 ,0.8, 0.3]
print sum(tank), sum(cost)
print gasStation(tank, cost)
print gasStation2(tank, cost)

