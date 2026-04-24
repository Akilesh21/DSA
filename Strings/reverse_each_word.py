def reverseWord(string,start,end):
    reverse =""
    while start < end :
        reverse = string[start] + reverse
        start +=1
    return reverse
string = "hello world" 
start = 0
end = len(string) 
print(reverseWord(string,start,end)) 
