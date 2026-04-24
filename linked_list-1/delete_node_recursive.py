class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def input_ll():
    l1 = [int(i) for i in input().split()]
    head = None
    tail = None
    for i in l1:
        node = ListNode(i)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node    
    return head        
def print_LL(head):
    while head is not None:
        print(head.val,"->",end=" ")
        head = head.next    
    print("None")     
    return     
class Solution:
    def mergeTwoLists(self,head1,head2):
        tail = head1.next
        while tail.next:
            tail = tail.next
        tail.next = head2
        return head1              
head1 = input_ll()
head2 = input_ll()
print_LL(head1)
print_LL(head2)
head_ = Solution().mergeTwoLists(head1,head2)
print_LL(head_)