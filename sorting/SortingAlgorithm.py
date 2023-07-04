import math

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

# cList = [2,1,7,6,5,3,4,9,8]

# selectionSort(cList)
 
 # Time complexity : O(n^2)
 # Space Complexity : O(1)


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key<customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    return customList


# cList = [2,1,7,6,5,3,4,9,8]
# insertionSort(cList)

# TIme Complexity : O(n^2)
# Space Complexity : O(1)

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k+=1
    return customList


# cList = [2,1,7,6,5,3,4,9,8]
# print(bucketSort(cList))

# Time Complexity: O(n^2) it can be improved
# Space Complexity: O(n)