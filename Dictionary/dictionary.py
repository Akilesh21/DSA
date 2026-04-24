a = {"the":1,"a":5,10000:"abc"}

print(type(a))

print(a)

print(len(a))

b=a.copy()
print(b)

c=dict([{"the",3},{"a",10},{2,3}])

print(c)

d=dict.fromkeys(["abc",32,4],10)

print(d)
dic = dict.fromkeys(["a","b",100,"hello"],10)
print(dic)
dic["b"] = 9
print(dic)
dic[100] = "hundred"
dic["hello"] = "world"
print(dic)