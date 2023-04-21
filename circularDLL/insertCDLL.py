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

    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location ==0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode
            return "The node has successfulyy created"


cirDLL = CircularDoublyLL()
print(cirDLL.createCDLL(5))
cirDLL.insertCDLL(0,0)
cirDLL.insertCDLL(1,-1)
cirDLL.insertCDLL(2,2)
print([node.value for node in cirDLL])