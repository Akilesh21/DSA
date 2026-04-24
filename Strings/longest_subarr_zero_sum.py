def subsetSum(l):
    list = []
    j = 0
    while j<len(l):
        for i in range(0,len(l)-1):
            list.append(j)
            
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))