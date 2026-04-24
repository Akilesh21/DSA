class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head = head.next       
    print("None")     
    return

def length(head) :
    #Your code goes here
    count = 0
    while head is not None:
        count +=1 
        head = head.next
    return count    

def insert_recursive(head,i,data):
    if i<0:
        return head    

    if i==0:
        newnode = Node(data)
        newnode.next = head
        return newnode

    if head is None:
        return None
    
    smallHead = insert_recursive(head.next,i-1,data)
    head.next = smallHead
    return head
def insert(head,i,data):
    if i<0 :
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count +=1    
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode    
    newNode.next = curr
    return head
        
def takeInput():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for curr_data in input_list:
        if curr_data == -1:
            break
        newnode = Node(curr_data)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
    return head
head = takeInput()    
printLL(head)
i = int(input())
data = int(input())
insert(head,i,data)
printLL(head)