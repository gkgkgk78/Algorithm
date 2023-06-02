import sys

input = sys.stdin.readline

n=int(input().rstrip())

dp=[[0]*(10) for _ in range(n+1)]

for i in range(0,10):
    dp[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        for k in range(0,j+1):
            dp[i][j]=dp[i][j]+dp[i-1][k]
            dp[i][j]=dp[i][j]%10007
sumz=0
for j in range(10):
    sumz+=dp[n][j]
print(sumz%10007)