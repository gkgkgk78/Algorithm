import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

if n<=1:
    print(0)
    sys.exit()
if n<=2:
    print(1)
    sys.exit()

dp = [1] * (n + 1)
for i in range(2, n + 1):
    now = i
    while now <= n:
        dp[now] += 1
        now += i
e = []
ans = 0
for i in range(2, n + 1):
    if dp[i] == 2:
        e.append(i)

left = 0
right = 1
now = e[0] + e[1]

while right < len(e):
    if now >= n:
        while now >= n:
            if now == n:
                ans += 1
            now -= e[left]
            left += 1
            if left == right:
                break

    else:
        right += 1
        if right == len(e):
            break
        now += e[right]

print(ans)