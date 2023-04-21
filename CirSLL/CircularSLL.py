class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CirSingLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "tThe CSLL has been created"


csll = CirSingLL()
csll.createCSLL(1)


print([node.value for node in csll])