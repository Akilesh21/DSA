def power_of_num(x,n):
    if n ==1:
        return x
    return  x * power_of_num(x,n-1)    
x,n = input().split()
x = int(x)
n = int(n)
print(power_of_num(x,n))