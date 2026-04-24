from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(head1, head2):

    # Write your code here
    if head1 is None and head2 is None:
        return
    if head2 is None:
        return head1
    if head1.data >= head2.data:  # h2 smaller
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    else:  # h1 smaller
        finalHead = head1
        finalTail = head1
        head1 = head1.next

    while head1 is not None and head2 is not None:
        if head1.data >= head2.data:  # h2 is smaller
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next

        else:  # h1 is smaller
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next

    while head1 is not None:
        finalTail.next = head1
        finalTail = finalTail.next
        head1 = head1.next

    while head2 is not None:
        finalTail.next = head2
        finalTail = finalTail.next
        head2 = head2.next

    return finalHead


def mid_point_node(head):
	if head is None :
		return None

	slow, fast = head, head

	while fast.next is not None and fast.next.next is not None :
		slow = slow.next
		fast = fast.next.next

	return slow


def mergeSort(head):
	if head is None or head.next is None:
		return head
	mid = mid_point_node(head)
	half1 = head
	half2 = mid.next
	mid.next = None
	half1 = mergeSort(half1)
	half2 = mergeSort(half2)
	return mergeTwoSortedLinkedLists(half1,half2)
#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
