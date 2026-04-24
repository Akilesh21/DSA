def linear_search(list,element):
    for i in range(0,len(list)):
        if element == list[i]:
            return i
    return -1
li = [1,2,3,4,7,9]
to_find = int(input())
ans = linear_search(list=li,element=to_find) 
print(ans)               