import sys

input = sys.stdin.readline
dp=[[0]*(10)for _ in range(65)]

for i in range(10):
    dp[1][i]=1

for i in range(2,65):
    for j in range(0,10):
        for k in range(0,j+1):
            dp[i][j]+=dp[i-1][k]
n=int(input().rstrip())
for _ in range(n):
    e=int(input().rstrip())
    sumz=0
    for i in range(10):
        sumz+=dp[e][i]
    print(sumz)