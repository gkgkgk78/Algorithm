import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input().rstrip())
total = []

for _ in range(n):
    e = list(map(int, input().split()))
    total.append(e)

dp = [[0] * (3) for _ in range(n)]
for i in range(3):
    dp[0][i] = total[0][i]
ans = sys.maxsize
# 이제 최솟값을 구해보도록 하자
for l in range(3):

    for i in range(3):
        if i == l:
            dp[0][i] = total[0][i]
        else:
            dp[0][i] = sys.maxsize
    for i in range(1, n):
        dp[i][0] = total[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = total[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = total[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i != l:
            ans = min(ans, dp[n - 1][i])
        else:
            continue

print(ans)