def multiplication(n,m):
    if m ==0:
        return 0
    answer = 0
    answer = n + multiplication(n,m-1)
    return answer    
from sys import setrecursionlimit
setrecursionlimit(2000)
n = int(input())
m = int(input())
print(multiplication(n,m))