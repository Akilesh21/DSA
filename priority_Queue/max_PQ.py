class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
class PriorityQueue:
    def __init__(self):
        self.pq = []
    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)    
    def isEmpty(self):
        #Implement the isEmpty() function here
        return self.getSize() == 0
    def getMax(self):
        #Implement the getMax() function here
        if self.isEmpty():
            return None
        return self.pq[0].value 
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex  = (childIndex -1)//2
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex    
            else:
                break
    def insert(self,value,priority):
        #Implement the insert() function here
        pqNode = PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2
        while leftChildIndex < self.getSize():
            maxIndex  = parentIndex
            if self.pq[maxIndex].priority < self.pq[leftChildIndex].priority:
                maxIndex = leftChildIndex
            if rightChildIndex < self.getSize() and self.pq[maxIndex].priority < self.pq[rightChildIndex].priority :
                maxIndex = rightChildIndex
            if maxIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[maxIndex] = self.pq[maxIndex],self.pq[parentIndex]
            parentIndex = maxIndex
            leftChildIndex = 2*parentIndex + 1
            rightChildIndex = 2*parentIndex + 2
    def removeMax(self):
        #Implement the removeMax() function here
        if self.isEmpty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele
pq = PriorityQueue()    
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)
for i in range(4):
    print(pq.removeMax())