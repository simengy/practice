import copy

class list:

    def __init__(self, value):
        
        self.value = value
        self.link = None
        self.head = self

    def add(self, value):
        
        curr = self.head
        
        while curr.link:
            curr = curr.link
        
        curr.link = list(value)
    

    def insert(self, value, pos):

        curr = self.head
        while curr:
            
            if curr.value == pos:
                
                temp = curr.link
                curr.link = list(value)
                curr = curr.link
                curr.link = temp

            curr = curr.link
   

    def remove(self, value):
        
        prev = None
        curr = self.head

        while curr:
            
            if curr.value == value:
                if prev is None:
                    prev = curr.link
                    self.head = curr.link
                else:
                    prev.link = curr.link
                
                curr = curr.link
            else:
                prev = curr
                curr = curr.link
        

    def printLst(self):
        
        curr = self.head
        if curr:
            print curr.value
 
            if curr.link:
                curr = curr.link
                curr.printLst()
            else:
                return


def reverse(node):
    
    if node.link is None:
        return node
       
    rList = reverse(node.link)
   
    rList.add(node.value)

    return rList


'''    
array = [3,2,3,4,5,6]
testLst = list(7)

for i in array:
    testLst.add(i)

testLst.printLst()

print 'REMOVING:'
testLst.remove(3)
testLst.remove(7)
testLst.printLst()

print 'REVERSING:'
temp = reverse(copy.deepcopy(testLst))
temp.printLst()
print 'omd'
testLst.printLst()

print 'Inserting:'
testLst.insert(11, 4)
testLst.printLst()
'''
