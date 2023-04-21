#1. Find the missing number in the array of 1 to 100 numbers.
import numpy as np
def missing_number(arr):
   #sum = n(n+1)/2
   sum_100 = 100*101/2
   miss_number = sum(arr)-sum_100
   return sum_100


arr = np.arrange(1,100)
np.delete(70,arr)
print(missing_number(arr))
