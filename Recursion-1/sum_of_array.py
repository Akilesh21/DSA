def sumArray(a,value):
    l = len(a)
    if l==0 or l==1:
        return a[0]
    new_list = a[1:]
    value  = a[0] + sumArray(new_list,value)
    return value    
    # Please add your code here
    pass
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
value = 0
print(sumArray(arr,value))
