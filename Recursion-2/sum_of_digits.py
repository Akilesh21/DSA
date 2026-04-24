#with recursion
def sum_of_digits(num):
    if len(num)==0 or len(num)==1:
        return num
    answer = 0
    small_num = sum_of_digits(num[1:])
    answer =int(small_num) + int(num[0])
    return answer
num  = input()
print(sum_of_digits(num))      
#without recursion
# digits = input()
# answer = 0
# for i in range(len(digits)):
#     answer += int(digits[i])
# print(answer)    