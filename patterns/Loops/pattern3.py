n = int(input())
#1st part
for i in range(1,n+1):
    for space in range(n,n-i+1,-1):
        print(" ",end="")    
    for num in range(i,n+1):
        print(num,end="")
    print()    
#2nd part        
for j in range(n-1,0,-1):
    for space in range(n,n-j+1,-1):
        print(" ",end="")  
    for num in range(j,n+1):
        print(num,end="")
    print()            