import list

def addTwoLists(lst1, lst2):

    count1 = 0
    count2 = 0

    curr = lst1.head
    while curr:
        curr = curr.link
        count1 += 1
    
    curr = lst2.head
    while curr:
        curr = curr.link
        count2 += 1

    if count1 > count2:
        N = count1
        while count2 < count1:
            lst2.add(0)
    else:
        N = count2
        while count1 < count1:
            lst1.add(0)

    print 'Alright!'

    lst1 = lst1.head
    lst2 = lst2.head
    lst = None

    while N > 0:
        
        N -= 1
        
        print N, lst1.value, lst2.value
        if lst is None:
            one = (lst1.value + lst2.value) % 10
            ten = (lst1.value + lst2.value) / 10
        else:
            one = (lst1.value + lst2.value + ten) % 10
            ten = (lst1.value + lst2.value + ten) / 10
        
        lst1 = lst1.link
        lst2 = lst2.link
        
        if lst:
            lst.add(one)
            
            if N == 0 and ten != 0:
                lst.add(ten)

        else:
            lst = list.list(one)
    
    return lst


lst1 = list.list(5)
lst1.add(4)
lst1.add(3)
lst1.printLst()

lst2 = list.list(7)
lst2.add(9)
lst2.add(2)
lst2.printLst()

print 'HERE'
lst = addTwoLists(lst1, lst2)
lst.printLst()


    
