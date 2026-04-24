def maxinmum_freq(s):
    d = {}
    max  = 0 
    for w in s:
        d[w] = d.get(w,0) + 1
    for w in d:
        if d[w] > max:
            max = d[w]
    for w in d :
        if max == d[w]:
            value = w
            break    
    return value                          

n = int(input())
s = [int(i) for i in input().split()]
print(maxinmum_freq(s))