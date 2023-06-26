import sys

input = sys.stdin.readline

n=int(input().rstrip())
dp=[0]*(n+1)
dp[0]=0
if n>=1:
    dp[1]=1
    for l in range(2,n+1):
        dp[l]=dp[l-1]+dp[l-2]
print(dp[n])