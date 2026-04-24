def lastIndexB(a,x,si):
    l=len(a)
    if si==l:
        return -1
    smallerListOutput=lastIndexB(a,x,si+1)
    if smallerListOutput!=-1:
        return smallerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
si =0
print(lastIndexB(arr, x,si))
