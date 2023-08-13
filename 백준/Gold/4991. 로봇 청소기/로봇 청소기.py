import sys
from collections import deque


def bfs(x, y, n, m, graph, rx, ry):
    visit = [[0] * (m) for _ in range(n)]
    q = deque()
    visit[x][y] = 1
    q.append((x, y, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x1, y1, count = q.popleft()
        if x1 == rx and y1 == ry:
            return count
        for i in range(4):
            zx = x1 + dx[i]
            zy = y1 + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if visit[zx][zy] == 0 and graph[zx][zy] != "x":
                    visit[zx][zy] = 1
                    q.append((zx, zy, count + 1))
    return -1


def perm(cnt, visit, check, last, total):
    if cnt == last:
        temp = []
        for i in check:
            temp.append(i)
        total.append(temp)
        return
    for i in range(last):
        if visit[i] == 1:
            continue
        visit[i] = 1
        check[cnt] = i
        perm(cnt + 1, visit, check, last, total)
        visit[i] = 0


while 1:
    a2, a1 = map(int, input().split())
    if a1 == 0 and a2 == 0:
        break
    graph = []
    dirty = []
    start = []
    for i in range(a1):
        e = list(map(str, input().rstrip()))
        for j in range(a2):
            if e[j] == "*":
                dirty.append([i, j])
            if e[j] == "o":
                start.append((i, j))
        graph.append(e)
    total = []
    visit = [0] * (len(dirty))
    check = [0] * (len(dirty))
    perm(0, visit, check, len(dirty), total)
    # 이제 순서 대로 해서 진행을 하면은 되겠다
    ans = sys.maxsize
    total1=[]
    wall=[[0]*(len(dirty))for _ in range(len(dirty))]
    for i in range(len(dirty)):
        nx=dirty[i][0]
        ny=dirty[i][1]
        for j in range(len(dirty)):
            if i==j:
                continue
            first = bfs(nx,ny, a1, a2, graph, dirty[j][0], dirty[j][1])
            wall[i][j]=first

    total2=[]
    dirty1=[]
    for i in dirty:
        first = bfs(start[0][0], start[0][1], a1, a2, graph, i[0], i[1])
        total2.append(first)

    for i1 in range(len(total)):
        temp = 0
        tt = 0
        fin=0
        if total2[total[i1][0]]==-1:
            continue
        for j in range(len(total[i1])-1):
            if wall[total[i1][j]][total[i1][j + 1]] == -1:
                fin = 1
                break
            temp+=wall[total[i1][j]][total[i1][j+1]]

        temp+=total2[total[i1][0]]
        if fin==0:
            ans = min(ans, temp)
    if ans != sys.maxsize:
        print(ans)
    else:
        print(-1)