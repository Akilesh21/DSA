import time
def power_of_num(x,n):
    if n ==0:
        return 1
    small_power = power_of_num(x,n//2)
    if n%2==0:
        return small_power * small_power
    else:
        return x * small_power * small_power 
from sys import setrecursionlimit
setrecursionlimit(11000)         
x,n = input().split()
x = int(x)
n = int(n)
print(time)
print(power_of_num(x,n))
print(time)
