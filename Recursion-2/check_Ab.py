def checkab(s):
    if len(s) == 0:
        return True
    if s[0] == "a":
        if len(s[1:]) > 1 and s[1:3] == "bb":
            return checkab(s[3:])
        else:
            return checkab(s[1:])
    else:
        return False


s = input()
if checkab(s) == True:
    print("true")
else:
    print("false")
