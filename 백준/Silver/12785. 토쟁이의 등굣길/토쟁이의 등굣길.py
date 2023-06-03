import sys
input = sys.stdin.readline

m, n = map(int, input().split())
y, x = map(int, input().split())
y -= 1
x -= 1
div = 1000007
dp = [[0] * (m) for _ in range(n)]

dp[0][0] = 1

for i in range(0, x + 1):
    for j in range(0, y + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
ct = dp[x][y]
for i in range(x, n):
    for j in range(y, m):
        if i == x or j == y:
            dp[i][j] = ct
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n - 1][m - 1] % div)