class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
class CircularSLL:
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

    def createCSLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        return "CSLL has been created"
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return "the head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode 
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while index<location-1:
                    node = node.next
                    index +=1
                newNode.next = node.next
                node.next = newNode
        return "The node has been successfully inserted"
    
    def deleteNode(self,location):
        if self.head is None:
            print('There is not any node in CSLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
                    
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None



cirSLL = CircularSLL()
print(cirSLL.createCSLL(1))
cirSLL.insertCSLL(0,0)

cirSLL.insertCSLL(2,1)

cirSLL.insertCSLL(3,1)

cirSLL.insertCSLL(5,-1)
print([node.value for node in cirSLL])

cirSLL.deleteNode(0)
print([node.value for node in cirSLL])
cirSLL.deleteEntireCSLL()
            
print([node.value for node in cirSLL])



