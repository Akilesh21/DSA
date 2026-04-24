from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reverse1(head):
    if head is None or head.next is None:
        return head
    smallHead = reverse1(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

def length(head):
    count = 0
    while head:
        count +=1
        head = head.next
    return count    


def kReverse(head, k) :
    if k ==0:
        return head
    if head is None or head.next is None:
        return head
    start_head = head
    prev = None
    
    for i in range(k):
        if start_head is not None:
            next_node = start_head.next
            start_head.next = prev
            prev = start_head
            start_head = next_node
        
    head.next  = kReverse(start_head,k)
    return prev
#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1