import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[[] for _ in range(m)] for _ in range(n)]
sx, sy = -1, -1

for i in range(n):
    e = list(map(str, input().rstrip()))
    for j in range(m):
        graph[i][j] = [e[j]]
        if e[j] == "I":
            sx, sy = i, j
        elif e[j] == ".":
            graph[i][j] = []

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

last = list(map(int, input().rstrip()))
count = 0
tx = [1, 1, 1, 0, 0, -1, -1, -1]
ty = [-1, 0, 1, -1, 1, -1, 0, 1]

for i1 in range(len(last)):
    zx = sx + dx[last[i1]]
    zy = sy + dy[last[i1]]
    if graph[zx][zy] == ["R"]:
        count = i1 + 1
        break
    else:
        graph[sx][sy] = []
        graph[zx][zy] = ["I"]
        sx = zx
        sy = zy
    temp = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == ["R"]:
                temp.append((i, j))
    for i, j in temp:
        nex = -1
        go = 1000
        for k in range(8):
            zx = i + tx[k]
            zy = j + ty[k]
            if 0 <= zx < n and 0 <= zy < m:
                mid = abs(zx - sx) + abs(zy - sy)
                if mid < go:
                    go = mid
                    nex = k
        zx = i + tx[nex]
        zy = j + ty[nex]
        if zx == sx and zy == sy:
            count = i1 + 1
            break
        else:
            if len(graph[i][j])>0:
                graph[i][j].pop()
            graph[zx][zy].append("R")
    if count != 0:
        break
    if count != 0:
        break
    # 폭발 시켜야지
    for i in range(n):
        for j in range(m):
            if len(graph[i][j]) >= 2:
                graph[i][j] = []
  

if count != 0:
    print("kraj " + (str)(count))
else:
    for i in range(n):
        answer = ""
        for j in range(m):
            if len(graph[i][j]) == 0:
                answer += "."
            else:
                answer += graph[i][j][0]
        print(answer)