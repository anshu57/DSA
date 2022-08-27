import numpy as np




def inver_arr(arr):
    arr_ret = arr
    for i,val in arr:
        arr_ret[val]=i
    return arr_ret

inver_arr([1,2,3,0,4])