import sys
def intersections(arr1, n, arr2, m) :
    #Your code goes here
    for i in range(n):
        for j in range(m):
            if arr1[i]==arr2[j]:
                print(arr1[i],end=' ')
                arr2[j]=sys.maxsize
                break
arr1 =[2,6,1,2]
arr2 = [1,2,3,4,2]
n = len(arr1)
m = len(arr2)
intersections(arr1,n,arr2,m)