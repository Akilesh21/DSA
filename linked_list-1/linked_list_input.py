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
def takeInput():
    input_list = [int(ele) for ele in input().split()]
    head = None
    for curr_data in input_list:
        if curr_data == -1:
            break
        newnode = Node(curr_data)
        if head is None:
            head = newnode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newnode
    return head
head = takeInput()    
print(head.next)