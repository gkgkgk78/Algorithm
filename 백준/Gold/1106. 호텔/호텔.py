import sys

input = sys.stdin.readline

c,n=map(int,input().split())
dp=[10**7]*(c+101)
dp[0]=0
for _ in range(n):
    a1,a2=map(int,input().split())
    for j in range(a2,c+101):
        dp[j]=min(dp[j],dp[j-a2]+a1)

print(min(dp[c:]))