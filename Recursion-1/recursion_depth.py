#Since we know that our machine have some limit for recursion to run in this vs code it is 998 and it will print error for 999 
#so we can incresase our recursion limit by using sys module and set a recursion limit let's see the example 
import sys 
sys.setrecursionlimit(10000)
def factorial(n):
    if n == 0 or n ==1 :
        return 1
    return n * factorial(n-1)
n = int(input())
print(factorial(n))    