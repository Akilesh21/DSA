def is_prime(n):
    for d in range(2,n):
        print(d)
        if (n%d==0):
            break
    else:
        return True

    return False    

n = int(input())
print(is_prime(n))           
