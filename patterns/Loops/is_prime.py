n = int(input())
flag = False
for d in range(2,n,1):
    if n%d==0:
        flag = True
if flag:
    print("not prime") 
else:
    print("prime")           