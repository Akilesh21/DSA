def return_all_subsequence(str):
    # base case
    if len(str) == 0:
        output = []
        output.append("")
        return output
    smallerString = str[1:]
    smallerOutput = return_all_subsequence(smallerString)
    output = []
    for sub in smallerOutput :
        output.append(sub)
    for sub in smallerOutput :
        output.append(str[0]+sub)    
    return output    
str = input()
print(return_all_subsequence(str))