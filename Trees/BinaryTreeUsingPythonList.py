# sing python list

class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size

# newBT = BinaryTree(8)

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value hass been successfully inserted"

# newBT = BinaryTree(8)
# print(newBT.insertNode("Drinks"))
# print(newBT.insertNode("Hot"))
# print(newBT.insertNode("Cold"))
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"
    
# newBT = BinaryTree(8)
# print(newBT.insertNode("Drinks"))
# print(newBT.insertNode("Hot"))
# print(newBT.insertNode("Cold"))
# print(newBT.searchNode("Hot"))

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 +1)

# newBT = BinaryTree(8)
# print(newBT.insertNode("Drinks"))
# print(newBT.insertNode("Hot"))
# print(newBT.insertNode("Cold"))
# print(newBT.insertNode("Tea"))
# print(newBT.insertNode("Coffee"))

# newBT.preOrderTraversal(1)
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 +1)



# newBT = BinaryTree(8)
# print(newBT.insertNode("Drinks"))
# print(newBT.insertNode("Hot"))
# print(newBT.insertNode("Cold"))
# print(newBT.insertNode("Tea"))
# print(newBT.insertNode("Coffee"))

# newBT.inOrderTraversal(1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])

# newBT = BinaryTree(8)
# print(newBT.insertNode("Drinks"))
# print(newBT.insertNode("Hot"))
# print(newBT.insertNode("Cold"))
# print(newBT.insertNode("Tea"))
# print(newBT.insertNode("Coffee"))

# newBT.postOrderTraversal(1)
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])


    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The node has been successfully deleted"
        

    def deleteBT(self):
        self.customList = None
        return "The BT has successfully deleted"

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

print(newBT.deleteBT())

newBT.levelOrderTraversal(1)




