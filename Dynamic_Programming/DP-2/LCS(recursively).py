def lcs(str1,str2,i,j):
    if i == len(str1) or j==len(str2):
        return 0
    if str1[i] == str2[j]:
        ans = 1 + lcs(str1,str2,i+1,j+1)
    else:
        ans1 = lcs(str1,str2,i+1,j) 
        ans2 = lcs(str1,str2,i,j+1)
        ans = max(ans1,ans2)
    return ans       

str1 = "abedgjc"
str2 = "bmdgsc"
i = 0
j = 0
ans =  lcs(str1,str2,i,j)
print(ans)