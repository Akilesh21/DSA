n=int(input())
for i in range(0,n):
    for j in range(n-i,0,-1):
        if(i%2==0):
            print(1,end="")
        else:
            print(0,end="")
    print()