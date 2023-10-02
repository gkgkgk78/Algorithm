import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    if i%2==1:
        dp[i]+=dp[i-1]
    else:
        dp[i]=dp[i-1]+dp[i//2]
    dp[i]%=1000000000
print(dp[n])