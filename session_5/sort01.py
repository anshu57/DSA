def sort01(arr):
    arr_new1=[]
    arr_new0=[]
    si=0
    ei=len(arr)-1
    while si<ei:
        if arr[si]==0:
            arr_new0.append(arr[si])
        elif(arr[si]==1):
            arr_new1.append(arr[si])
        elif(arr[ei]==0):
            arr_new0.append(arr[si])
        elif(arr[ei]==1):
            arr_new1.append(arr[si])
        si+=1
        ei-=1
    return(arr_new0 + arr_new1)
arr=[]
arr=int(input().split(' '))
sort01(arr)