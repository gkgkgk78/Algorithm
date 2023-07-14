import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())

tree = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
for _ in range(n - 1):
    a1, a2 = map(int, input().split())
    tree[a1].append(a2)
    tree[a2].append(a1)


def dfs(v):
    dp[v] = 1
    for i in tree[v]:
        if dp[i] == 0:
            dfs(i)
            dp[v] += dp[i]


dfs(r)
for _ in range(q):
    a = int(input().rstrip())
    print(dp[a])