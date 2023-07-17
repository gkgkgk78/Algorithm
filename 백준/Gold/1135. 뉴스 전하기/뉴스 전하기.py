import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * (n)
visit = [0] * (n)
graph = [[] for _ in range(n)]
e = list(map(int, input().split()))
for i in range(1, len(e)):
    graph[e[i]].append(i)
count = [0] * (n + 1)


def dfs(v):
    visit[v] = 1
    next = []

    for a2 in graph[v]:
        dfs(a2)
        next.append(dp[a2])
    if next:
        next.sort(reverse=True)
        dp[v] = 0
        t = 0
        last = []
        for i in next:
            t += 1
            last.append(i + t)
        dp[v] = max(last)
    else:
        dp[v] = 0


visit = [0] * (n)
dfs(0)

print(max(dp))