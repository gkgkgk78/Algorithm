import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
e = []
k = int(input().rstrip())
for _ in range(k):
    a1, a2, a3, a4 = map(int, input().split())
    e.append((a1, a2, a3, a4))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0]=1

def check(bx, by, ax, ay):
    for (t1, t2, t3, t4) in e:
        if (bx, by, ax, ay) == (t1, t2, t3, t4) or (ax, ay, bx, by) == (t1, t2, t3, t4):
            return 0
    return 1


for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            continue
        # 확인 해보도록 하자
        if j > 0:
            x, y = i, j - 1
            cc = check(x, y, i, j)
            if cc == 1:
                dp[i][j] += dp[i][j - 1]
        if i > 0:
            x, y = i-1, j
            cc = check(x, y, i, j)
            if cc == 1:
                dp[i][j] += dp[i-1][j]

print(dp[n][m])