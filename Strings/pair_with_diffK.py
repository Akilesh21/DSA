def printPairDiffK(l, k):
    count  = 0
    for i in range(len(l)):
        for j in range(len(l)-1):
            if (l[i] - l[j+1]) == k or (l[i] - l[j+1]) == -k:
                count +=1  
    return count
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))