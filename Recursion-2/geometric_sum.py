def geometric_sum(n):
    if n == 0:
        return 1
    answer = geometric_sum(n-1)
    return answer + (1/(2**n))



n = int(input())
print(format(geometric_sum(n),'.5f'))
