def check_armstrong(num):
    sum = 0
    order = len(str(num))

    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num==sum:
        return True 
    else:
        return False  
num = int(input(""))             
is_armstrong = check_armstrong(num)
if is_armstrong:
    print("true")
else:
    print("false")    