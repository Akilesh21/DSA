class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next



node1 = Node(10)
node2 = Node(20)
node3 = Node(20)
print(node1)
print(node2)
print(node3)