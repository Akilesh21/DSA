
from sys import stdin
def binarySearch(arr, n, x) :
    #Your code goes here
    result = -1
    l = 0
    u = len(arr)-1
    median  = (l+u)//2
    for i in range(n):
        if arr[median] == x:
            result = median
            u = median - 1
        elif arr[median] >x:
            u = median -1
            if l>u:
                return result
        else:
            l = median+1
    return result      
li =  [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
x = int(input())
n = len(li) 
search = binarySearch(li,n,x)
if search !=-1:
    print(f'The first occurrence of element {x} is located at index {search}')
else:
    print("element is not present in the list")