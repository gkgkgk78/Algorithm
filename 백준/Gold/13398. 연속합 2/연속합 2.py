import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
ans=-sys.maxsize
dp=[[-10**6]*(2) for _ in range(n)]
dp[0][0]=e[0]
ans=max(ans,dp[0][0])

for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+e[i],e[i])
    dp[i][1]=max(dp[i-1][1]+e[i],dp[i-1][0])
    ans=max(ans,dp[i][0],dp[i][1])
print(ans)