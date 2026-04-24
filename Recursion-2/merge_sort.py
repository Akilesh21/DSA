#merge sort using recursive
def merge(arr1,arr2,a):
    i = 0
    j =0
    k = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            a[k] = arr1[i]
            k +=1
            i +=1
        else:
            a[k] = arr2[j]
            k +=1
            j +=1    
    while i<len(arr1):
        a[k] = arr1[i]
        k = k+1
        i = i+1
    while j<len(arr2):
        a[k] = arr2[j]
        k = k+1
        j = j+1

def mergeSort(arr):
    if len(arr) ==0 or len(arr) ==1:
        return 
    # Please add your code here
    mid = len(arr)//2
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    mergeSort(arr1)
    mergeSort(arr2)
    merge(arr1,arr2,arr)
    return arr
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))

mergeSort(arr)
for x in arr:
    print(x,end=' ')
print()    