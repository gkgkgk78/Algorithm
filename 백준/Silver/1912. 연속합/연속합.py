import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
ans=-sys.maxsize
dp=[-1001]*(n)
dp[0]=e[0]
ans=max(ans,dp[0])
for i in range(1,n):
    dp[i]=max(e[i]+dp[i-1],e[i])
    ans=max(dp[i],ans)
print(ans)