def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)

arr = [int(x) for x in input().split()]
x = int(input())
si = 0
ei = len(arr)-1
print(binarySearch(arr,x,si,ei))