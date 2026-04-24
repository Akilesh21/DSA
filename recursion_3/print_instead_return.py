# Factorial
def PrintFactorial(n,ans):
    if n ==0:
        print(ans)
        return
    ans = ans * n
    PrintFactorial(n-1,ans)
PrintFactorial(5,1)    
# Fibonaaci 
# def fibo(n,m,ans):
#     if n == 0 or n == 1 and m ==0 or m ==1:
#         print(ans)
#         return 
#     ans = ans + n + m
#     fibo(n-1,m-2,ans)
# fibo(2,2,1)

