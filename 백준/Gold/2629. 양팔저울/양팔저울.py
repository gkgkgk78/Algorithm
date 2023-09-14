import sys

input = sys.stdin.readline

n = int(input().rstrip())
goo = list(map(int, input().split()))
m = int(input().rstrip())
cho = list(map(int, input().split()))

dp = [[0] * (15001) for _ in range(31)]
weight = [0] * (31)
for i in range(len(goo)):
    weight[i] = goo[i]


def dfs(val, wei):  # 확인한 추의 개수, 무게

    if val > n:
        return
    if dp[val][wei] == 1:
        return

    dp[val][wei] = 1
    dfs(val + 1, wei + weight[val])
    dfs(val + 1, abs(wei - weight[val]))
    dfs(val + 1, wei)

dfs(0, 0)

ans = []
for i in cho:
    if i > 15000:
        ans.append("N")
        continue
    if dp[n][i] == 1:
        ans.append("Y")
    else:
        ans.append("N")
print(*ans)