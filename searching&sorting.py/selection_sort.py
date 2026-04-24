def SelectionSort(arr):
    for i in range(len(arr)):
        min_value = i   
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_value]:
                min_value = j
        arr[i],arr[min_value] = arr[min_value],arr[i]
    return arr        
li = [13,4,9,5,3]
n = len(li)
print(SelectionSort(li,n))