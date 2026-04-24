def checkMember(n):
    list = []
    n1  = 0
    n2=1
    count = 0
    if n <= 1:
       n=1
    else:
        while count < n:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            list.append(nth)
            count += 1
        if n in list:
            return True
        else:
            return False        

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")