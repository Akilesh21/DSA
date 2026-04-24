def Rotatearray(arr,n,d):
    arr = arr[d:] + arr[0:d]
    return arr 
li = [0,1,2,3,4,5,6,7] 
n = len(li)
d = int(input())

print(Rotatearray(li,n,d))          