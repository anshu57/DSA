class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def inserSLL(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif location == -1:
            self.tail.next = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head.next
            self.head = newNode
        else:
            tempNode = self.head
            index = 0
            while index<location-1:
                tempNode = tempNode.next
                index+=1
            newNode.next = tempNode.next
            tempNode.next = newNode

    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None

sinll = SinglyLL()
sinll.inserSLL(1,-1)
sinll.inserSLL(2,-1)
sinll.inserSLL(3,-1)
sinll.inserSLL(4,-1)

sinll.inserSLL(0,0)
sinll.inserSLL(0,3)
print([node.value for node in sinll])
sinll.deleteEntireSLL()
print([node.value for node in sinll])

