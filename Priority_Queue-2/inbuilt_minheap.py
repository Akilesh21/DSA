import heapq
li = [5,1,4,8,7,9,11]
heapq.heapify(li)
heapq.heappush(li,3)
print(li)
heapq.heappop(li)
print(li)
heapq.heapreplace(li,6)
print(li)