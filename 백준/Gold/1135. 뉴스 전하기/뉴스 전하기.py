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

def dfs(v):
    visit[v] = 1
    next = []

    for a2 in graph[v]:
        if visit[a2] == 1:
            continue
        dfs(a2)
        next.append(dp[a2])
    if next:
        next.sort(reverse=True)
        t = 0
        last = []
        for i in next:
            t += 1
            last.append(i + t)
        dp[v] = max(last)


dfs(0)
print(max(dp))