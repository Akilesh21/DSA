#soln 1
def reverse_list1(arr):
   li = []
   for i in range(-1,-len(arr)-1,-1):
       li.append(arr[i])
   return li   

def reverse_list2(arr):
    for i in range(len(arr)//2):
        arr[i] , arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    return arr      
li = [1,2,3,4,5,7,8,9]
li = reverse_list1(li)
li = reverse_list2(li)
print(li)