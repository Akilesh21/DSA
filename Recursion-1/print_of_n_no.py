#print 1 to n
def print_n_no(n):
    if n ==0:
        return 0
    print_n_no(n-1)
    print(n)
n = int(input())
print_n_no(n)

#print n to 1
# def print_n_no(n):
#     if n ==0:
#         return
#     print(n)     
#     print_n_no(n-1)
# n = int(input())
# print_n_no(n)