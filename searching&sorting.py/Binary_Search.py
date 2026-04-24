
from sys import stdin
def binarySearch(arr, n, x) :
    #Your code goes here
    l = 0
    u = len(arr)-1
    median  = (l+u)//2
    for i in range(n):
        if arr[median] == x:
            return median
        elif arr[median] >x:
            u = median -1
            median = (l+u)//2
            if l>u:
                return -1
        else:
            l = median+1
            median = (l+u)//2
    return -1        
li =  [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
x = int(input())
n = len(li) 
print(binarySearch(li,n,x))