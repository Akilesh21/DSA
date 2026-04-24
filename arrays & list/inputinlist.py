n = int(input("Enter the size of list you want="))
def sum(arr):
    total = 0
    for i in range(len(arr)):
        total =total + arr[i]
    return total
li = []    
for add in range(1,n+1):
    li.append(add)
value_of_sum = sum(li)    
print(value_of_sum)

