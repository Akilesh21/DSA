class Node:
    def __init__(self,head):
        self.head = head
        self.next = None
def takeInput():
    head = None
    tail = None

    datas =[int(ele) for ele in input().split()]

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head
