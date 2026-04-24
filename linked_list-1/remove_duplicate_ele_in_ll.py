class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


def printLL(head):
  while head is not None:
    print(str(head.data) + "->",end = "")
    head = head.next
  print("None")
  return  


def removeDuplicates(head) :
    if head is None or head.next is None:
        return head
   
    curr = head
    adv = curr.next
   
    while adv is not None:
        if curr.data == adv.data:
            curr.next = adv.next
            adv = curr.next
        else:
            curr = curr.next
            adv = adv.next
           
    return head
def takeInput():
  input_list = [int(ele) for ele in input().split()]  
  head = None
  tail = None
  for curr_data in input_list:
    if curr_data ==-1:
      break
    new_node = Node(curr_data)  
    if head is None:
      head = new_node
      tail = new_node
    else:
      tail.next = new_node
      tail = new_node  
  return head        

head = takeInput()
printLL(head)
head = removeDuplicates(head)
printLL(head)

