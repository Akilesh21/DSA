def insertionsort(arr,n):
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
                i-=1    
    return arr   

li = [int(x) for x in input().split()]
n  = len(li)
print(insertionsort(li,n))
