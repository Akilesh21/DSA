n = int(input())
i =1
while i<=n:
    spaces = 1
    while spaces <=n-i:
        print(" ",end='')
        spaces =spaces+1
    p=1    
    j=1  
    if i%2==1: 
        while  j <=i:
            print("*",end="")
            p=p+1
            j=j+1
    print() 
    i=i+1       