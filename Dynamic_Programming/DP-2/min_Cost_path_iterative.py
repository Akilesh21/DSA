import sys
def minCostIterative(cost,n,m):
    
    dp=[[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=cost[i][j]
            else:
                ans1=dp[i+1][j]
                ans2=dp[i][j+1]
                ans3=dp[i+1][j+1]
                dp[i][j]=cost[i][j]+min(ans1,ans2,ans3)
    return dp[0][0]
cost=[[1,5,11],[8,3,12],[2,3,7]]
n=3
m=3 
ans=minCostIterative(cost,n,m)
print(ans)
