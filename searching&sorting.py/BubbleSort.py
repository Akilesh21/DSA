def BubbleSort(arr,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        j-=1
    return arr    
li = [9,3,6,2,0] 
n = len(li)
print(BubbleSort(li,n))               