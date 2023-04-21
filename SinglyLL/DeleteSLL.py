class Node:
    def __init__(self, value):
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

    def inserSLL(self,value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head.next
            self.head = newNode
        elif location ==-1:
            self.tail.next = newNode
            self.tail = newNode
        else:
            node = self.head
            index = 0
            while index < location -1:
                node = node.next
                index+=1
            newNode.next = node.next
            node.next = newNode

    def transversal(self):
        if self.head is None:
            print('The list is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def deleteSLL(self,location):
        if self.head is None:
            print('The linked list does not exist')
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node.next !=self.tail:
                    node = node.next
                node.next = None
                self.tail = node
        else:
            node = self.head
            index = 0
            while index<location-1:
                node = node.next
                index += 1
            node.next = node.next.next



sinll = SinglyLL()
sinll.inserSLL(1,-1)
sinll.inserSLL(2,-1)
sinll.inserSLL(3,-1)
sinll.inserSLL(4,-1)

sinll.inserSLL(0,0)
sinll.inserSLL(0,3)

print([node.value for node in sinll])
sinll.deleteSLL(3)
print([node.value for node in sinll])















            