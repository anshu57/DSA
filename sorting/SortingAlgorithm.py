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

def merge(customList, l, m, r):
    n1 = m-l+1
    n2 = r-m

    L = [0]*n1 
    R = [0]*n2 
    for i in range(0, n1):
        L[i] = customList[l+i]

    for j in range(0, n2):
        R[j] = customList[m+1+j]

    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            customList[k] = L[i]
            i+=1
        else:
            customList[k] = R[j]
            j +=1
        k+=1

    while i<n1:
        customList[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        customList[k] = R[j]
        j+=1
        k+=1

def mergeSort(customList, l,r):
    if l<r:
        m = (l+(r-1))//2
        mergeSort(customList, l,m)
        mergeSort(customList, m+1,r)
        merge(customList, l, m, r)
    return customList

# cList = [2,1,7,6,5,3,4,9,8]

# print(mergeSort(cList, 0, 8))

# Time Complexity : O(NlogN)
# Space Complexity : O(N)


def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2],  my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index +=1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quicksort(my_list, left, right):
    if left<right:
        pivot_index = pivot(my_list, left, right)
        quicksort(my_list, left, pivot_index-1)
        quicksort(my_list, pivot_index+1, right)


my_list = [3,5,0,6,2,1,4]

print(quicksort(my_list, 0, 6))
print(my_list)
