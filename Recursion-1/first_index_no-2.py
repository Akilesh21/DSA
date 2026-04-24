# using 2 way of solving same sum in better way
def firstIndex_better(arr,x,si):
    l =len(arr)
    if arr[si] ==x:
        return si
    elif si ==l-1:
        return -1
    si_index = firstIndex_better(arr,x,si+1) 
    return si_index     
from sys import setrecursionlimit
setrecursionlimit(10000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
si = 0
print(firstIndex_better(arr,x,si))