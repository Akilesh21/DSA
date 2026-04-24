def uniqueChar(s): 
    list = []
    for i in s:
        list.append(i)
    length = len(list)    
    # Write your code here
    for i in range(length):
        for j in range(length-1):
            if list[i] == list[j+1]:
                list.pop(j+1)
                length -=2
    for k in list:
        print(k,end="")





# Main 
s=input() 
uniqueChar(s)