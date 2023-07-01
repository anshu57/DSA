class Heap:
    def __init__(self, size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size + 1
#Time Complexity : O(1)
#Space Complexity : O(n)


def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
#Time complexity : O(1)
# Space ?complexity: O(1) 

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize   
# Time Complexity : O(1)
# Space Complexity : O(1)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

#Time Complexity : O(n)
#Space Complexity : O(1)

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# Time Complexity : O(logn)
# Space Complexity : O(log n) 

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is fail"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
# Time Complexity : O(log N)
# Space Complexity : O(log N)


# newHeap = Heap(5)
# insertNode(newHeap, 4, "Max")
# insertNode(newHeap, 5, "Max")
# insertNode(newHeap, 2, "Max")
# insertNode(newHeap, 1, "Max")
# levelOrderTraversal(newHeap)

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index *2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize <leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customlist[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customlist[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize ==0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
    
newHeap = Heap(5)
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
print(extractNode(newHeap, "Max"))

# Time Complexity : O(LogN)
# Space Complexity : O(LogN)
    


