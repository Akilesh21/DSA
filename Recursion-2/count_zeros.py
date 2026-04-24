def count_zeros(number):
    if number== 0 :
        return 1
    
    if number == 1:
        return 0 
    
    if number //10 == 0:
        return 0
    
    small_answer = count_zeros(number//10)
    last_digit = number%10
    if last_digit ==0:
        return small_answer +1
    else:
        return small_answer
number = int(input())      
      
print(count_zeros(number))