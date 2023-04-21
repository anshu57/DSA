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

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    def transverseSLL(self):
        if self.head is None:
            print("The singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
            

sinll = SinglyLL()
sinll.insertSLL(1,-1)
sinll.insertSLL(2,-1)
sinll.insertSLL(3,-1)
sinll.insertSLL(4,-1)

sinll.insertSLL(0,0)

sinll.insertSLL(0,3)

print([node.value for node in sinll])
sinll.transverseSLL()