def bubbleSort(customList):
    for i in range(len(customList)):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1], customList[j]

    print(customList)

# cList = [2,1,5,6,3,7,9,4]

# bubbleSort(cList)

# Time Complexity : O(n^2)
# Space Complexity : O(1)

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

cList = [2,1,7,6,5,3,4,9,8]

selectionSort(cList)
 