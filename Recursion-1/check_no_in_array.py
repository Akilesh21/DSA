def checkNumber(arr, x):
    l = len(arr)
    # Please add your code here
    if l ==0 :
        return False
    elif l==1:
        if arr[0] ==x :
            return True    
    if arr[0] == x:
        return True        
    new_list = arr[1:]
    check_list_no = checkNumber(new_list,x)
    return check_list_no
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
