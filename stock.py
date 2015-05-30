# one-time sell and buy
# Fix this: there is constraint that T_max > T_min
def buysell1(stock):

    min = None
    maxP = None

    for i in xrange(len(stock)):


        if min is None:
            min = i
        elif stock[min] > stock[i]:
            min = i

        if maxP < stock[i] - stock[min]:
            maxP = stock[i] - stock[min]

    return maxP, min


def buysell2(stock):
    
    buy = None
    profit = 0
    for i in xrange(len(stocks)-1):

        if stock[i+1] - stock[i] > 0 and buy is None:

            buy = stock[i]

        if stock[i+1] - stock[i] < 0 and buy:
            print stock[i], buy
            profit += stock[i] - buy
            buy = None

    return profit

def buysell3(stock):
    
    min = None
    maxP = None
    oldMaxP = [0] * len(stock)

    for i in xrange(len(stock)):

        if min is None:
            min = i
        elif stock[min] > stock[i]:
            min = i

        if maxP < stock[i] - stock[min]:
            maxP = stock[i]- stock[min]

        oldMaxP[i] = maxP 
    
    maxP = None
    max = None
    for i in xrange(len(stock)-1, -1, -1):
        
        if max is None:
            max = stock[i]
        elif max < stock[i]:
            max = stock[i]

        if maxP < max - stock[i] + oldMaxP[i]:
            maxP = max - stock[i] + oldMaxP[i]
    
    return maxP

stocks = [4,3,4,5,3,8,10,6,1,5,9,2] 
print stocks
print buysell1(stocks)
print buysell2(stocks)

stocks = [1,2,4,2,5,7,2,4,9] 
print buysell3(stocks)

