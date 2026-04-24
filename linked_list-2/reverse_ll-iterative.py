class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_3(head):
    curr = head 
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head      


def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head = head.next       
    print("None")     
    return
def takeInput():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail =  None
    for curr_data in input_list:
        if curr_data == -1:
            break
        newnode = Node(curr_data)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail =  newnode
    return head
head = takeInput()    
printLL(head)
head =reverse_3(head)
printLL(head)