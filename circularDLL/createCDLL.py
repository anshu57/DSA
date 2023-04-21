class Node:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.next = None
        self.prev = None

class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return 'The CDLL is created successfully'

cirDLL = CircularDoublyLL()
print(cirDLL.createCDLL(5))
print([node.value for node in cirDLL])