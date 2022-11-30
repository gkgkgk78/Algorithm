import sys
 
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
array = list(map(int, input().split()))
 
dp = [0] * (n + 1)
for _ in range(n):
    dp[_ + 1] = dp[_] + array[_]
 
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])