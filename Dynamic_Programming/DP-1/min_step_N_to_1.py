from sys import stdin,setrecursionlimit
from sys import maxsize as MAX_VALUE
setrecursionlimit(10**6)

# recurive solution
# def countMinStepsToOne(n,dp) :
#     if n==1:
#         return 0
#     ans1=100000
#     if n% 3==0:
#         if dp[n//3]==-1:
#             ans1=countMinStepsToOne(n//3,dp)
#             dp[n//3]=ans1
#         else:
#             ans1=dp[n//3]
#     ans2=100000
    
#     if n%2==0:
#         if dp[n//2]==-1:
#             ans2=countMinStepsToOne(n//2,dp)
#             dp[n//2]=ans2
#         else:
#             ans2=dp[n//2]
#     if dp[n-1]==-1:
#         ans3=countMinStepsToOne(n-1,dp)
#         dp[n-1]=ans3
#     else:
#         ans3=dp[n-1]
    
#     ans=1+min(ans1,ans2,ans3)
#     return ans
# iterative solution
def countMinStepsToOne(n):
    dp = [-1 for i in range(n+1)]
    dp[1] = 0

    for i in range(2, n+1):
        ans1, ans2, ans3 = MAX_VALUE, MAX_VALUE, MAX_VALUE

        if i % 3 == 0:
            ans1 = dp[i//3]
        if i % 2 == 0:
            ans2 = dp[i//2]
        ans3 = dp[i-1]

        dp[i] = 1 + min(ans1, ans2, ans3)

    return dp[n]




#main
n = int(stdin.readline().rstrip())
dp = [-1 for i in range(n+1)]
print(countMinStepsToOne(n))