class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): 
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "Doubly LL is created successfuly"

doublyLL = DoublyLL()
doublyLL.createDLL(5)
print([node.value for node in doublyLL])
