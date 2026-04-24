# Problem: Remove x from string
def removeX(string):
    l = len(string) 
    if l ==0:
        return string
    removeX_string = removeX(string[1:])        
    if string[0]!="x":
        removeX_string =string[0] + removeX_string
    return removeX_string
# Main
string = input()
print(removeX(string))