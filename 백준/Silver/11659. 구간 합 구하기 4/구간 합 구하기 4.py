import sys

input = sys.stdin.readline
n,m=map(int,input().split())
li=list(map(int,input().split()))

dp=[0] *(n+1)
dp[1]=li[0]
for i in range(2,n+1):
    dp[i]=dp[i-1]+li[i-1]

for _ in range(m):
    a1,a2=map(int,input().split())
    print(dp[a2]-dp[a1-1])
