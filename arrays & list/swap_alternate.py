def swap_Alternate(arr):
    i = 0
    for k in range(len(arr)//2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
        i = i+2
    return print(arr)
li = [1,2,3,4,5,6]
li = swap_Alternate(li)