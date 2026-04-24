def checkMaxHeap(lst):
    parentindex = 0
    while parentindex < len(lst):
        leftchildindex = 2*parentindex + 1
        rightchildindex = 2*parentindex + 2
        maxindex = parentindex
        if leftchildindex < len(lst) and lst[parentindex] < lst[leftchildindex]:   
            maxindex = leftchildindex
        if rightchildindex < len(lst) and lst[maxindex] < lst[rightchildindex]:
            maxindex = rightchildindex
        if maxindex == parentindex:
            parentindex += 1
        else:
            return False  
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')

