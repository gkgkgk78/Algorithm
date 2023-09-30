import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
a1, a2 = map(int, input().split())
k = int(input().rstrip())
dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

e = []

for _ in range(k):
    e.append(int(input().rstrip()))


def dfs(index, x, y):
    # print(index)
    if index == k:
        return 0

    val = e[index]

    dp[val][x][y] = min((dfs(index + 1, val, y) + abs(val - x))
                          , (dfs(index + 1, x, val) + abs(val - y)))
    return dp[val][x][y]


print(dfs(0, a1, a2))