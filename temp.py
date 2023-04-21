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
        while node is not None:
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

    def transverSLL(self):
        if self.head is None:
            print('The singly linkedlist does not exist')
        else:
            node =self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self,value):
        if self.head == None:
            print('SinglyLinkedList does not exist')
        else:
            node = self.head
            while node is not None:
                if value == node.value:
                    return node.value
                else:
                    node = node.next
            return 'The value does not exist in list'