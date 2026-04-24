class Queue:
    def __init__ (self):
        self.__queue =[]
        self.__count = 0
        self.__front = 0
    def enqueue(self,element):
        self.__queue.append(element)
        self.__count += 1
    def dequeue(self):
        if self.isempty():
            return  -1
        element = self.__queue[self.__front]
        self.__count -=1 
        self.__front +=1
        return element
    def front(self):
        if self.__count ==0:
            return -1
        return self.__queue[self.__front]      
    def size(self):
        return self.__count
    def isempty(self):
        return self.size() ==0    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.isempty())
print(q.front())
print(q.size())
q.dequeue()
print(q.front())