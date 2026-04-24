import math,sys
sys.setrecursionlimit(10**6)
def minStepsTo1(n,dp):
    if n ==0:
        return 0
    ans = 100
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        if dp[n-(i**2)] == -1:
            currAns = 1 + minStepsTo1(n-(i**2),dp)
            dp[n-(i**2)] = currAns
        else:    
            currAns = dp[n-(i**2)]
        ans = min(ans,currAns)
    return ans    
n = int(input())
dp = [-1 for i in range(n+1)]
print(minStepsTo1(n,dp))
