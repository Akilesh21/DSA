import heapq
def kthLargest(lst, k):
    heap = lst[0:k]
    heapq.heapify(heap)
    for i in range(k,len(lst)):
        if heap[0] < lst[i]:
            heapq.heapreplace(heap,lst[i])          
    heap.reverse()
    return heap[k-1]

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)

# different approach
