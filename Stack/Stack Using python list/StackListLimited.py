class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the list"
        else:
            return self.list[-1]
        


    def delete(self):
        self.list = None




customstack = Stack(4)

print(customstack.isEmpty())
print(customstack.isFull())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)

        
