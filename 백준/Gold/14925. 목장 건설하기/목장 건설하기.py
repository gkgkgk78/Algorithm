import sys

input = sys.stdin.readline
ans=0
n,m=map(int,input().split())
graph=[]
dp=[[0]*(m+1)for _ in range(n+1)]
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(1,n+1):
    for  j in range(1,m+1):
        if graph[i-1][j-1]==0:
            dp[i][j]= min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
            ans=max(ans,dp[i][j])
print(ans)