# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    # Please add your code here
        if len(s) == 0 or len(s) == 1:
            return s
        if s[0]==s[1]:
            smallOutput = removeConsecutiveDuplicates(s[1:])
            return smallOutput
        else:
            smallOutput = removeConsecutiveDuplicates(s[1:])
            return s[0]+smallOutput
   

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
