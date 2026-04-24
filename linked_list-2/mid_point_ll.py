class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None

def mid_point(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data    

def printLL(head):
    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print("None")
    return    

def takeinput():
    input_list = [int(ele) for ele in input().split()] 
    head = None
    tail = None
    for curr_data in input_list:
        if curr_data == -1:
            break
        new_node = Node(curr_data)
        if head is None:
            head = new_node
            tail =  new_node
        else:
            tail.next = new_node
            tail = new_node
    return head            
head = takeinput()
print(mid_point(head))    