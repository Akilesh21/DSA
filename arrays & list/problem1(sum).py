n = input()
str = input()
str_split = str.split()
li = []
for x in str_split:
    li.append(int(x))
value = 0
for sum in li:
    value =value + sum
print(value)    