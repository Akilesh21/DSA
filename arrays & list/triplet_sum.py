def pair_sum(arr,n,x):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] + arr[j+1] == x:
                count+=1
    return count 
li = [1,3,6,2,5,4,3,2,4]
n = len(li) 
x = int(input()) 
print(pair_sum(li,n,x))         