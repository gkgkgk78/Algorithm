import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    e = list(map(int, input().split()))
    k = int(input().rstrip())
    dp = [0] * (k + 1)
    dp[0]=1
    for i in range(n):
        now=e[i]
        for j in range(now,k+1):
            dp[j]+=dp[j-now]
    print(dp[k])