def getstring(d):
    if d == 2:
        return "abc"
    if d ==3:
        return "def"
    if d ==4:
        return "ghi"
    if d ==5:
        return "jkl"
    if d ==6:
        return "mno"
    if d ==7:
        return "pqrs"
    if d ==8:
        return "tuv"
    if d ==9:
        return "wxyz"
def Printkeypad(n,output):
    #Implement Your Code Here
    if n == 0:
        print(output)
        return
    smallerNumber = n//10
    lastDigit = n%10
    optionsForlastDigit = getstring(lastDigit)  
    for c in optionsForlastDigit:
        newoutput = c + output 
        Printkeypad(smallerNumber,newoutput)       



n = int(input())
Printkeypad(n,"")