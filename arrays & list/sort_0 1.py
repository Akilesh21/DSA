from sys import stdin

def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    i = 0
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[i], arr[j]
        elif arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        i+=1
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
