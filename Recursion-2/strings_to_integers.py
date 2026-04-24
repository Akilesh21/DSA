from sys import setrecursionlimit
setrecursionlimit(11000)

def strings_to_int(string):
    if len(string) == 0:
        return
    if len(string) == 1:
        return int(string)  # convert string to int
    small_string = strings_to_int(string[1:])
    new_string = ""
    if string[0] == "0":
        new_string += str(small_string)
    else:
        new_string = int(string[0])*10**(len(string)-1) + int(small_string)  # convert string to int and multiply by 10 to the power of the length of the string
    return new_string

string = input()
print(strings_to_int(string))