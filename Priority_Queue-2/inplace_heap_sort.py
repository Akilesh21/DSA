def down_heapify(arr,i,n):
    parentIndex = i
    leftchildindex = 2*parentIndex + 1
    rightchildindex = 2*parentIndex +2
    while leftchildindex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftchildindex]:
              minIndex = leftchildindex
        if rightchildindex < n and arr[minIndex] >arr[rightchildindex] :
              minIndex = rightchildindex
        if minIndex == parentIndex:
              break
        arr[minIndex],arr[parentIndex] = arr[parentIndex],arr[minIndex]    
        parentIndex = minIndex
        leftchildindex = 2*parentIndex +1
        rightchildindex = 2*parentIndex +2


def heapSort(arr):
        #  Building the heap
        n = len(arr)
        for i in  range(n//2,-1,-1):
              down_heapify(arr,i,n)
        # Removing n elements from heap and put them at correct position
        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            down_heapify(arr,0,i)   
        return arr               
n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')