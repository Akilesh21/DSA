class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]     
        self.count = 0
    def size(self):
        return self.count
    def getBucketIndex(self,hc):
        return (abs(hc)) % (self.bucketSize)
    def getValue(self,key):
        hash_code = hash(key)
        index = self.getBucketIndex(hash_code)
        head = self.buckets[index]
        while head is not None:
            if head.key ==key:
                return head.value
            head = head.next
        return None    
    def remove(self,key):
        hash_code = hash(key)
        index = self.getBucketIndex(hash_code)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -=1    
                return head.value
            prev = head    
            head = head.next

        return None 
    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2 * self.bucketSize 
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next
    def loadfactor(self):
        return self.count/self.bucketSize            
    def insert(self,key,value):
        hash_code = hash(key)
        index = self.getBucketIndex(hash_code)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next   
        head = self.buckets[index]    
        newNode = MapNode(key,value)
        newNode.next = head    
        self.buckets[index] = newNode
        self.count +=1 
        loadFactor  = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()
m = Map()
# m.insert('Akhilesh',2)
# print(m.size())
# m.insert('Krishna',1)
# print(m.size())
# m.insert('Akhilesh',3)
# print(m.size())
# print(m.getValue('Akhilesh'))
# print(m.remove('Akhilesh'))
# print(m.getValue('Akhilesh'))
# print(m.size())

for i in range(20):
    m.insert('abc'+str(i),i+1)
    print(m.loadfactor())
for i in range(20):
    print('abc'+str(i) + ':',m.getValue('abc'+str(i)))