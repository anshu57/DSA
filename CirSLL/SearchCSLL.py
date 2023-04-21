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

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
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


    def transversalCSLL(self):
        if self.head is None:
            print("ther is no element for transversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
#Searching for CSLL

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"

        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The Node does not exist in this CSLL"



cirSLL = CircularSLL()
print(cirSLL.createCSLL(1))
cirSLL.insertCSLL(0,0)

cirSLL.insertCSLL(2,1)

cirSLL.insertCSLL(3,1)

cirSLL.insertCSLL(5,-1)
cirSLL.transversalCSLL()
print(cirSLL.searchCSLL(4))
