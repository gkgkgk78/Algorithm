import sys

input = sys.stdin.readline
div=10**9
n = int(input().rstrip())
dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(n+1)]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(1<<10):
            if j==0:
                dp[i][j][(1<<j)|k] += dp[i - 1][j + 1][k]
            elif j==9:
                dp[i][j][(1<<j)|k] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][(1<<j)|k] += dp[i - 1][j - 1][k]
                dp[i][j][(1<<j)|k] += dp[i - 1][j + 1][k]
            dp[i][j][(1<<j)|k]%=div
ans=0
for i in range(1,10):
    ans+=dp[n][i][(1<<10)-1]
    ans%=div
print(ans)