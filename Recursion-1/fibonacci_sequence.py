def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0    
    fib_n_1=fib(n-1)
    fib_n_2=fib(n-2)  
    output=fib_n_1+fib_n_2
    return output

n=int(input())
for i in range(n):
    print(fib(i+1))