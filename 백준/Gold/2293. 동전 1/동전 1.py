import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
e = []
for _ in range(n):
    a = int(input().rstrip())
    if a <= k:
        e.append(a)
dp = [0] * (k + 1)
dp[0] = 1
for i in range(len(e)):
    now = e[i]
    for j in range(now, k + 1):
        dp[j] += dp[j - now]
print(dp[k])