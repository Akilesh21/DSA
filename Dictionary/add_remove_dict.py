a={1:2,3:4,"list":[1,23],"dict":{1:2}}
a['t']=(1,2,3)
print(a)
a[1]=10
print(a)
b={3:5,'the':4,2:100}
a.update(b)
print(a)
a.pop('t')
print(a)
del a[1]
print(a)
a.clear()
print(a)
del a # it will delete the dictionay or any value
s = {1,2,3,5,4,2,3,1}
print(len(s),end= " ")
s.add(4)
s.add(3)
print(len(s))
