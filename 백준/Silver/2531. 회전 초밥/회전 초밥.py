import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
e = []
for _ in range(n):
    e.append(int(input().rstrip()))
dp = [0] * (d + 1)

ans = -sys.maxsize
dp[c] += 1
now = 1

for i in range(k):
    if dp[e[i]] == 0:
        now += 1
    dp[e[i]] += 1
left = 0
right = k - 1

for _ in range(n):

    right += 1
    if right == n:
        right = 0

    if dp[e[right]] == 0:
        now += 1
    dp[e[right]] += 1

    if dp[e[left]] == 1:
        now -= 1
    dp[e[left]] -= 1
    left += 1
    if left == n:
        left = 0
    ans = max(ans, now)

print(ans)