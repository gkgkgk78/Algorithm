import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visit = [[-1] * (m) for _ in range(n)]
graph = []
for _ in range(n):
    e = list(map(int, input().rstrip()))
    graph.append(e)
ans = -sys.maxsize


def check(visit):
    global ans
    visit1 = [[0] * (m) for _ in range(n)]
    ne = 0
    for i in range(n):
        for j in range(m):
            if visit1[i][j] == 1:
                continue
            temp = ""
            zx = i
            zy = j
            if visit[i][j] == 0:
                # 가로
                while 1:
                    if visit[zx][zy] == 1:
                        break
                    visit1[zx][zy] = 1
                    temp += str(graph[zx][zy])
                    zy += 1
                    if zy == m:
                        break
            else:
                while 1:
                    if visit[zx][zy] == 0:
                        break
                    visit1[zx][zy] = 1
                    temp += str(graph[zx][zy])
                    zx += 1
                    if zx == n:
                        break
            ne += (int)(temp)
    ans = max(ans, ne)


def dfs(x, y, visit):
    if (x == n - 1 and y == m):
        check(visit)
        return
    zx = x
    zy = y
    if zy == m:
        zx += 1
        zy = 0
    # 가로
    visit[zx][zy] = 0
    dfs(zx, zy + 1, visit)
    # 세로
    visit[zx][zy] = 1
    dfs(zx, zy + 1, visit)

dfs(0, 0, visit)
print(ans)