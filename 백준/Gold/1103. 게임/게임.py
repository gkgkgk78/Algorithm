import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visit = [[0] * (m) for _ in range(n)]
dp = [[0] * (m) for _ in range(n)]
for _ in range(n):
    e = list(map(str, input().rstrip()))
    graph.append(e)
ans = -sys.maxsize


def dfs(x, y, count):
    global ans

    if not (0 <= x < n and 0 <= y < m):
        return 1
    if graph[x][y] == "H":
        return 1
    if visit[x][y] == 1:
        print(-1)
        exit()
    if dp[x][y] != 0:
        return dp[x][y]+1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    now = (int)(graph[x][y])
    visit[x][y] = 1
    for i in range(4):
        zx = x + dx[i] * now
        zy = y + dy[i] * now
        dp[x][y]=max(dp[x][y],dfs(zx,zy,count))
    visit[x][y] = 0
    ans = max(ans, dp[x][y])
    return dp[x][y]+1


dfs(0, 0, 0)

print(ans)