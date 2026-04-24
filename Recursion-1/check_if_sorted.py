# check whether the list is sorted or not
def isSorted(a,l):
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    isSmallerListSorted=isSorted(a[1:],l-1)
    return isSmallerListSorted

a=[int(x) for x in input().split()]
l = len(a)
print(isSorted(a,l))

#so now we will make a better looking code for check the sorting
def isSortedBetter(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted=isSortedBetter(a,si+1)
    return isSmallerPartSorted

a=[1,2,3,4,5,6,7,8,9]
isSortedBetter(a,0)

