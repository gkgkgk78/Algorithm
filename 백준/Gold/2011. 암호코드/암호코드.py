import sys


input = sys.stdin.readline
e=str(input().rstrip())
n=list(map(int, e))
last = int(e)
if n[0] == 0:
    print(0)
else:
    n = [0] + n
    dp = [0] * (len(n) + 1)
    dp[0] = 1
    for i in range(1, len(n)):
        now = n[i]
        if 1 <= now <= 9:
            dp[i] += dp[i - 1]
        be = n[i - 1]
        nex = be * 10 + now
        if 10 <= nex <= 26:
            dp[i] += dp[i - 2]

    print(dp[len(e)] % 1000000)