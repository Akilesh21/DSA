import heapq
li = [1,2,3,4,5,6,7]
heapq._heapify_max(li)
print(li)
heapq._heappop_max(li)
print(li)
heapq._heapreplace_max(li,9)
print(li)
li.append(11)
