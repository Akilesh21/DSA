# using 1 way of solving that is creating spacing
def firstIndex(arr, x,k):
    # Please add your code here
    l = len(arr)
    if l == 0:
        return -1
    if arr[0]==x:
        return k   
    new_list = arr[1:] 
    k+=1
    k_index = firstIndex(new_list,x,k)    
    return k_index   

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
k = 0
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,k))
