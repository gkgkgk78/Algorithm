import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1  # 시작 볼륨을 의미함

e = list(map(int, input().split()))
for i in range(1, n + 1):
    now = e[i - 1]
    for j in range(m + 1):
        if dp[i - 1][j] > 0:
            next = j + now
            next1 = j - now
            if 0 <= next <= m:
                dp[i][next] += dp[i - 1][j]
            if 0 <= next1 <= m:
                dp[i][next1] += dp[i - 1][j]

ans = -sys.maxsize
for i in range(m + 1):
    if dp[n][i] > 0:
        ans = i
if ans == -sys.maxsize:
    print(-1)
else:
    print(ans)