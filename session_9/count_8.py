def count_8(num):
    if num == 0:
        return 0
    counts = count_8(num//10)
    
    return counts if (num %10 !=8) else counts+1

# count hi in a string
def count_hi(str):
    
    if len(str)<2:
        return 0
    if str[0]=='h' and str[1]=='i':
       return count_hi(str[2:])+1
    else:
        return count_hi(str[1:])
# Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.
def count_hi2(str):
    
    if len(str)<2:
        return 0
    if str[0]=='x' and str[1]=='h' and str[2]=='i':
       return count_hi2(str[3:])
    elif str[0]=='h' and str[1]=='i':
        return count_hi2(str[2:]) + 1
    else:
        return count_hi2(str[1:])

# Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

def changePi(str):
    if len(str)<2:
        return str
    if str[0]=='p' and str[1] == 'i':
        return '3.14'+changePi(str[2:])
    else: 
        return str[0]+changePi(str[1:])

# Display List Using Recursion

# display List using Recursion
def display(arr, idx):
    if idx == len(arr):
        return

    print(arr[idx])
    display(arr, idx + 1)


# display List in reverse order using Recursion
def displayReverse(arr, idx):
    if idx == len(arr):
        return

    displayReverse(arr, idx + 1)
    print(arr[idx])


def findData(arr, idx, data):
    if idx == len(arr):
        return False

    return arr[idx] == data or findData(arr, idx + 1, data)


def maximum(arr, idx):
    if idx == len(arr):
        return -math.inf

    return max(arr[idx], maximum(arr, idx + 1))

# https://leetcode.com/problems/fibonacci-number/
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#  https://leetcode.com/problems/n-th-tribonacci-number/
def tribonacci(self, n: int) -> int:
    if n ==0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)




    
    
