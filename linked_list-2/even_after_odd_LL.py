from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    if head.next is None:
        return head
    
    odd_head  = None
    odd_tail  = None
    even_head = None
    even_tail = None
    
    current =  head 
    while current is not None:
        if current.data % 2 !=0 : # odd
            
            if odd_head is None:
                odd_head = current
                odd_tail = current
                
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            
            current = current.next
            
        
        else:    #even
            if even_head is None:
                even_head = current
                even_tail = current
            
                
            else:
                even_tail.next = current
                even_tail = even_tail.next
            
            current = current.next
    
    if odd_tail:
        odd_tail.next = even_head
    
    if even_tail:
        even_tail.next = None
    else:
        odd_tail.next = None
    
    
    if odd_head is None:
        return even_head
    else:
        return odd_head
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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    new_head = evenAfterOdd(head)
    printLinkedList(new_head)  
    
    t -= 1