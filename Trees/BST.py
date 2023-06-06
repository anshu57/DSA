
import sys
sys.path.insert(0, '/home/anshu/Desktop/data/DSA_udemy')

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild =BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The Node has been successfully inserted"


# newBST = BSTNode(None)
# print(insertNode(newBST, 70))
# print(insertNode(newBST,30))
# print(newBST.data)
# print(newBST.leftChild.data)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)




# preOrderTraversal(newBST)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# newBST = BSTNode(None)
# print(insertNode(newBST, 70))
# print(insertNode(newBST,30))
# insertNode(newBST,50)
# insertNode(newBST,20)
# insertNode(newBST,10)
# insertNode(newBST,180)
# insertNode(newBST,40)

# inOrderTraversal(newBST)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,30)
insertNode(newBST,50)
insertNode(newBST,20)
insertNode(newBST,10)
insertNode(newBST,180)
insertNode(newBST,40)

postOrderTraversal(newBST)

from Queue import QueueLinkedList as queue


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,30)
insertNode(newBST,50)
insertNode(newBST,20)
insertNode(newBST,10)
insertNode(newBST,180)
insertNode(newBST,40)

levelOrderTraversal(newBST)

