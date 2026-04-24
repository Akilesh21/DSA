#with recursion
def check_pakindrome(string):
    if len(string) == 0 or len(string) ==1:
        return string
    reverse = ""
    small_string = check_pakindrome(string[1:])
    reverse = small_string + string[0]
    return reverse
string = input()
if string == check_pakindrome(string):
    print("true") 
else:
    print("false")       

#without recursion
# string = input()
# reverse = ""
# for i in range(len(string)-1,-1,-1):
#     reverse +=string[i]
# if string ==reverse:
#     print("true")     
# else:
#     print("false")    