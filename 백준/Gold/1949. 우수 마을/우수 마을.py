import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input().rstrip())
total = [0]
e = list(map(int, input().split()))
total.extend(e)
dp = [[0] * (2) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(n - 1):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)


# 0 우수마을 x, 1: 우수마을

def dfs(vertex):
    visit[vertex] = 1
    dp[vertex][0] = 0
    dp[vertex][1] = total[vertex]

    for i in graph[vertex]:
        if visit[i] == 1:
            continue
        dfs(i)
        dp[vertex][0] += max(dp[i][0], dp[i][1])
        dp[vertex][1] += dp[i][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))