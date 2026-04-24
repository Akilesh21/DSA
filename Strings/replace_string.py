def replace_string(string,char,want_char):
    replace_string =""
    for i in range(len(string)):
        if string[i] == char :
            replace_string += want_char
        else:
            replace_string +=string[i]
    return replace_string       
string = input("choose a string:") 
char = input("which char you want to replace in string:") 
want_char = input("char you want in replace of  previous char:") 
new_String = replace_string(string,char,want_char) 
print(new_String)     