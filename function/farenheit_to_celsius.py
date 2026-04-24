def printTable(start,end,step):
    while start<=end:
        celsius  = int((start-32)*5/9)
        print(start,celsius)
        start = start+step
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
