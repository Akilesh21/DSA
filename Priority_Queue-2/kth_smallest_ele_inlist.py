import heapq
def kSmallest(lst, k):
    heap = lst[0:k]
    heapq._heapify_max(heap)
    for i in range(k,len(lst)):
        if heap[0] > lst[i]:
            heapq._heapreplace_max(heap,lst[i])          
    return heap
# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')