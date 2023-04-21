class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully appended"
    
    def pop(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack.peek())

print(customstack.isempty())
print(customstack)