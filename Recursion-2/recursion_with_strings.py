def replace_string(string,a,b):
    if len(string) == 0:
        return string
    small_output_list = replace_string(string[1:],a,b)
    if string[0]==a:
        return b + small_output_list
    else:
        return string[0] + small_output_list
string = "abcd" 
print(replace_string(string,"a","x"))           

