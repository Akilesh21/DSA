#Q remove a index element in the list without using pop and remove

def remove_ele(string,l,index):
    new_list = ""
    for i in range(l):
        if i != index :
            new_list +=str(string[i]) + " "
    list =  new_list.split(" ")
    l2 = [] 
    for j in range(len(list)-1):
        l2.append(int(list[j]))
    return l2    
    
new_loop = 0
n = int(input())
while new_loop<n:
    li = [int(x) for x in input().split(" ")]
    l = len(li)
    index = int(input())
    print(remove_ele(li,l,index))
    new_loop+=1
    