# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        li1 = ""
        while l1 is not None:
            li1 += str(l1.val) 
            l1 = l1.next
        li2 = ""
        while l2 is not None:
            li2 += str(l2.val) 
            l2 = l2.next
        li3 = str(int(li1) + int(li2))
        li4 = []
        for i in range(len(li3)-1,0):
            li4.append(int(li3[i]))
        new_head = None
        new_tail = None
        for i in li4:
            new_node = ListNode(i)
            if new_head is None:
                new_head = new_node
                new_tail = new_node
            else:
                new_tail.next = new_node
                new_tail = new_node
        return new_head                       
