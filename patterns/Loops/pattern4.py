n = int(input())
#1st part
n1 = int((n+1)/2)
for i in range(1,n1+1,1):
    for spaces in range(0,n1-i):
        print(" ",end="")
    for stars in range(0,2*i-1):
        print("*",end="")    
    print()    
#2nd part
n2 = n1-1
for j in range(n2,0,-1):
    for spaces in range(n2-j+1,0,-1):
        print(" ",end="")
    for stars in range(2*j-1,0,-1):
        print("*",end="")
    print()        