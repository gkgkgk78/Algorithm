import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
k=int(input().rstrip())

dp=[[0]*(k+1)for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][1]=i
    dp[i][0]=0

for i in range(2,n):
    for j in range(2,k+1):
        dp[i][j]=(dp[i-1][j]+dp[i-2][j-1])%1000000003

if k==1:
    print(n%1000000003)
else:
    print((dp[n-1][k]+dp[n-3][k-1])%1000000003)