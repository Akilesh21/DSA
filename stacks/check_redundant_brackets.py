
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
    s = []
    for curr in expression:
        if curr == ")":
            pass
        else:
            s.append(curr)
    return s        
#main
expression = stdin.readline().strip()
print(checkRedundantBrackets(expression))
# if checkRedundantBrackets(expression) :
# 	print("true")

# else :
# 	print("false")
