def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(1,l-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr

def bubble_sort_02(arr):
    l = len(arr)
    flag = 1
    for i in range(l):
        for j in range(1,l-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                flag = 0
        if flag == 1:
            return arr
    return arr

# time : O(n2) and space : O(1)
def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i+1,l):
            if arr[j-1]<arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


# avg case T: O(n) and worst case T:O(n2)
def insertion_sort(arr):
    l = len(arr)
    for i in range(1,l):
        for j in range(i,-1,-1):
           if arr[j-1]>arr[j]:
            arr[i-1],arr[i] = arr[i],arr[i-1]
           else:
            break
    return arr



def merge_two_sorted_list(A,B):
  myAns = []
  i, j =0,0
  while i<len(A) and j<len(B):
    if A[i]<B[j]:
      myAns.append(A[i])
      i+=1
    else:
      myAns.append(B[j])
      j+=1
  while j< len(B):
    myAns.append(B[j])
    j+=1
  
  while i< len(A):
    myAns.append(A[i])
    i+=1
  return myAns

def merge_sort(arr,si,ei):
    if ei==si:
        return arr[si]
    mid = (ei+ei)//2
    leftsidemerge = merge_sort(arr,si,mid)
    rightsidemerge = merge_sort(arr,mid+1,ei)
    
    merge_two_sorted_list(leftsidemerge,rightsidemerge)
    return arr

def merge_sort01(arr):
    si = 0
    ei = len(arr)
    return merge_sort(arr,si,ei)

