a = "Akhilesh soni"
# for i in range(len(a)):
    # print(a[i])
#Q check whether the s is present in the string if it is so how many it is present 
string_count = 0
is_true = False
string = input()
for i in a:
    if i==string: 
        is_true = True
        string_count +=1
if is_true:
    print(f"Yes it is {string} is present in the string and {string_count} is total no of {string} present")
else:
    print("not present")            
