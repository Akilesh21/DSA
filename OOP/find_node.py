# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    c =0
    # Write your code here.
    while head:
        if head.data==n:
            return c   
        head = head.next 
        c=c+1      
    else:
        return -1    
def takeInput():
    input_list = [int(ele) for ele in input().split()] 
    head = None
    tail = None
    for curr_ele in input_list:
        if curr_ele ==-1:
            break
        new_node = Node(curr_ele)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head            
head = takeInput()
n = int(input())
print(findNode(head,n))