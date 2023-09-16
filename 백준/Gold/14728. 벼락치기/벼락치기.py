import sys

input = sys.stdin.readline

n,c=map(int,input().split())
dp=[0]*(c+1)

for _ in range(n):
    a2,a1=map(int,input().split())
    for j in range(c,a2-1,-1):
        dp[j]=max(dp[j],dp[j-a2]+a1)

print(dp[c])