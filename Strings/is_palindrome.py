def isPalindrome(string,n):
    new_string = ""
    for i in range(n-1,-1,-1):
        new_string =new_string + string[i]
        if new_string == string:
            return True
    else:
        return False 
string = input()
n = len(string)
print(isPalindrome(string,n))