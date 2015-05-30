from list import list

class Tree:

    def __init__(self, value, left=None, right=None):

        self.left = left
        self.right = right
        self.value = value

    def add(self, value):

        newNode = Tree(value)
        curr = self

        while curr is not None:
        
            if value <= curr.value:
                if curr.left is None:
                    curr.left = newNode
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = newNode
                    break
                else:
                    curr = curr.right
                    
    def printNode(self):

        curr = self
        if curr is None:
            return

        print curr.value

        if curr.left:
            print 'left:'
            curr.left.printNode()
        if curr.right:
            print 'right:'
            curr.right.printNode()

        
def max_depth(node):
    
    depth = 0
    
    if node is None: 
        return depth
    
    d1 = max_depth(node.left)
    d2 = max_depth(node.right)
    if d1 > d2:
        depth = d1 + 1
    else:
        depth = d2 + 1

    return depth


def totalsum(node):
       
    if node is None:
        return 0
    
    total = node.value
    if node.left is not None:
        total += totalsum(node.left)
    if node.right is not None:
        total += totalsum(node.right)

    return total


def pathsum(tree, num):
    
    path = [] 
    res = num - tree.value
    if tree.left is None and tree.right is None:
        if res == 0:
            path.append(tree.value)
            return path
        else:
            return None
    elif tree.left:
        path = pathsum(tree.left, res)
        if path:
            path.append(tree.value)
            return path
    elif tree.right:
        path = pathsum(tree.right, res)
        if path:
            path.append(tree.value)
            return path

    return None


def levelPrint(tree, nodes, level):
    
    if tree:        
        if level not in nodes:
            nodes[level] = [tree.value,]
        else:
            nodes[level].append(tree.value)
        
        if tree.left == None and tree.right == None:
            return nodes

        if tree.left:
            levelPrint(tree.left,nodes,level+1)
        if tree.right:
            levelPrint(tree.right,nodes,level+1)
    else:
        return


def sortedListToTree(List):
    
    test = None

    while List:

        if test is None:

            test = Tree(List.value)
        else:
            test.add(List.value)

        List = List.link

    return test
    
def inorder(tree):

    lst = []

    if tree:
        if tree.left == None and tree.right == None:
            return [tree.value, ]
        
        if tree.left:
            lst.extend(inorder(tree.left))

        lst.append(tree.value)
        
        if tree.right:
            lst.extend(inorder(tree.right))
            
    return lst


def leastCommonAncestor(tree, node1, node2):
    
    curr = tree
    
    while curr:
        if node1 > curr.value and node2 > curr.value:
            curr = curr.right
            continue
        elif node1 < curr.value and node2 < curr.value:
            curr = curr.left
            continue
        else:
            return curr


array = [32, 21, 43, 25, 72, 11, 13, 29, 27]

lst = list(30)
for i in array:
    lst.add(i)

print 'SAMPLE'
lst.printLst()
test = sortedListToTree(lst)
test.printNode()

print 'inorder:'
print inorder(test)

print 'lca:'
print leastCommonAncestor(test, 11, 32).value

'''
testTree = Tree(30)

for i in array:
    testTree.add(i)

testTree.printNode()
print sum(array)
print totalsum(testTree)
print 'PATHSUM = ', pathsum(testTree, 75)
print max_depth(testTree)

# breadth first
nodes = {}
levelPrint(testTree, nodes, 1)
for key in nodes:
    print key, nodes[key]
'''
