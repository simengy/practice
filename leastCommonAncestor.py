import random
import tree

def findNode(node, value):
    if node is None:
        return None
    elif node.value == value:
        return node
    else:
        results = findNode(node.left, value)
        if results:
            return results
        
        results = findNode(node.right, value)
        if results:
            return results


def leastCommonAncestor2(node, value1, value2):

    print 'DEBUG:', node.value
    if node.value==value1 or node.value==value2:
        return node

    if findNode(node.left, value1) and findNode(node.left, value2):
        return leastCommonAncestor2(node.left, value1, value2)
    elif findNode(node.right, value1) and findNode(node.right, value2):
        return leastCommonAncestor2(node.right, value1, value2)
    else:    
        return node
    

if __name__ == '__main__':

    print '\n'
    print 'RUNNING Test:'

    Node = tree.Tree(10)
    tmp = [7,8,2,13,15]
    for i in xrange(len(tmp)):
        Node.add(tmp[i])
    
    Node.printNode()
    print 'We have found', findNode(Node, 7).value, findNode(Node, 7).left.value
    nd = leastCommonAncestor2(Node, 2, 8)
    print 'Ancestor is:', nd.value


