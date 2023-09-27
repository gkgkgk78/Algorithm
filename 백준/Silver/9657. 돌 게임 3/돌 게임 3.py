import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1
for i in range(4, n + 1):

    if dp[i - 1] + dp[i - 3] + dp[i - 4] < 3:
        dp[i] = 1

if dp[n] == 1:
    print("SK")
else:
    print("CY")