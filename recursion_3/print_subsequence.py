# Here we will print the all subsequence instead of returning it
def printSubs(s,o):
    if len(s)==0:
        print(o)
        return 
    # don't include the Oth char
    printSubs(s[1:],o)
    # include the 0th char
    newOutput = o + s[0]
    printSubs(s[1:],newOutput)
printSubs("abc","")