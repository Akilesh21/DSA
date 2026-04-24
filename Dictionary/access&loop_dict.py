a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a)

print(a['list'])
a.get('list')
print(a.get("li"))
print(a.get('li',0))
print(a.keys())
print(a.values())
print(a.items())

for i in a:
    print(i,a[i]) #i =will give keys only and a[i] will give the values

for i in a.values():
    print(i)

print("list" in a)

print(2 in a)