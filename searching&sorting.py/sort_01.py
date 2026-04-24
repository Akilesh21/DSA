from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
                i-=1    
    for ans in arr:
        print(ans,end=" ") 
    print()     
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list



#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    
    t -= 1
