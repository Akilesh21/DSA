import sys
def min_cost_path(cost,i,j,n,m,dp):
    
    # special case
    if i==n-1 and j==m-1:
        return cost[i][j]
    # Base case 
    if i>=n or j>=m:
        return sys.maxsize
    if dp[i][j+1] == sys.maxsize:
        ans1 = min_cost_path(cost,i,j+1,n,m,dp)
        dp[i][j+1] = ans1
    else:    
        ans1 = dp[i][j+1]
    if dp[i+1][j] == sys.maxsize:    
        ans2 = min_cost_path(cost,i+1,j,n,m,dp)
        dp[i+1][j] = ans2
    else:
        ans2 = dp[i+1][j] 
    if dp[i+1][j+1] == sys.maxsize:     
        ans3 = min_cost_path(cost,i+1,j+1,n,m,dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]   
    ans = cost[i][j] + min(ans1,ans2,ans3)
    return ans

cost = [[1,5,11],[8,13,12]]
# memoization
n = 4
m = 3
dp = [[sys.maxsize for j in range(m+1)] for i in range(n+1)]
ans = min_cost_path(cost,0,0,2,3,dp)
print(ans)