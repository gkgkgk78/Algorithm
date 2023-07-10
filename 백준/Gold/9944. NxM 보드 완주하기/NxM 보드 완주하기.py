import sys

input = sys.stdin.readline

ans = sys.maxsize


def check(graph, visit, n, m, dir, x, y):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    zx = x + dx[dir]
    zy = y + dy[dir]
    if 0 <= zx < n and 0 <= zy < m:
        if visit[zx][zy] == 0 and graph[zx][zy] == ".":
            return 1
    return 0


def dfs(graph, visit, x, y, count, vi_count, dir, n, m):
    global ans

    if count > ans:  # count는 변경 횟수
        return
    if vi_count == 0:  # 남은 빈칸 갯수
        ans = min(ans, count)

        return
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    zx = x + dx[dir]
    zy = y + dy[dir]
    if 0 <= zx < n and 0 <= zy < m:
        if graph[zx][zy] == "." and visit[zx][zy]==0:
            visit[zx][zy] = 1
            dfs(graph, visit, zx, zy, count, vi_count - 1, dir, n, m)
            visit[zx][zy] = 0
        else :
            # 방향 바꿔야함
            for i in range(4):
                if i == dir:
                    continue
                t = check(graph, visit, n, m, i, x, y)
                if t == 1:
                    tx = x + dx[i]
                    ty = y + dy[i]
                    visit[tx][ty] = 1
                    dfs(graph, visit, tx, ty, count + 1, vi_count - 1, i, n, m)
                    visit[tx][ty] = 0
    else:
        for i in range(4):
            if i == dir:
                continue
            t = check(graph, visit, n, m, i, x, y)
            if t == 1:
                tx = x + dx[i]
                ty = y + dy[i]
                visit[tx][ty] = 1
                dfs(graph, visit, tx, ty, count + 1, vi_count - 1, i, n, m)
                visit[tx][ty] = 0
tt=1
while 1:
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    try:
        e = list(map(int, input().split()))
        if len(e) == 0:
            break
        ans = sys.maxsize
        n, m = e[0], e[1]
        graph = []
        total = []
        visit = [[0] * (m) for _ in range(n)]
        for i in range(n):
            te = list(map(str, input().rstrip()))
            for j in range(m):
                if te[j] == ".":
                    total.append((i, j))
            graph.append(te)

        for a1, a2 in total:
            visit[a1][a2]=1
            for i in range(4):
                if (check(graph, visit, n, m, i, a1, a2)):
                    dfs(graph, visit, a1, a2, 1, len(total)-1, i, n, m)
            if len(total)-1==0:
                ans=0
            visit[a1][a2]=0
        if ans==sys.maxsize:
            print("Case "+str(tt)+": "+"-1")
        else:
            print("Case "+str(tt)+": "+str(ans))
        tt+=1
    except:
        break