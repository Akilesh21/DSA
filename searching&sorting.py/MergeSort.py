def mergeSort(arr1,n,arr2,m):
    i =0
    j=0
    arr3 = []
    while (i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i = i+1
        else:
            arr3.append(arr2[j])
            j=j+1
    while (i<len(arr1)):
        arr3.append(arr1[i])
        i = i+1 
    while (j<len(arr2)):
        arr3.append(arr2[j])
        j=j+1            
    return arr3
arr1 = [int(x) for x in input().split()] 
arr2 = [int(y) for y in input().split()] 
n = len(arr1)
m = len(arr2)  
print(mergeSort(arr1,n,arr2,m))               

