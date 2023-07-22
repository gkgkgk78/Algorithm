import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

for _ in range(r):
    e = list(map(str, input().rstrip()))
    graph.append(e)

go = int(input().rstrip())
e = list(map(int, input().split()))


def de(graph, x, dir):
    x = r - x
    if dir == 0:
        # 왼쪽
        for j in range(0, c):
            if graph[x][j] == "x":
                graph[x][j] = "."
                return 1
                break
    else:
        for j in range(c - 1, -1, -1):
            if graph[x][j] == "x":
                graph[x][j] = "."
                return 1
                break

    return 0


def bfs(x, y, visit, graph):
    q = deque()
    visit[x][y] = 1
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            zx = x1 + dx[i]
            zy = y1 + dy[i]
            if 0 <= zx < r and 0 <= zy < c and graph[zx][zy] == "x" and visit[zx][zy] == 0:
                visit[zx][zy] = 1
                q.append((zx, zy))


def move(x, y, graph, visit):
    q = deque()
    visit[x][y] = 1
    temp = []
    temp.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((x,y))
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            zx = x1 + dx[i]
            zy = y1 + dy[i]
            if 0 <= zx < r and 0 <= zy < c and graph[zx][zy] == "x" and visit[zx][zy] == 0:
                visit[zx][zy] = 1
                q.append((zx, zy))
                temp.append((zx, zy))
    for x1, y1 in temp:
        graph[x1][y1]="."
    #이제 집합을 다 구했으니 내리면 된다
    while 1:
        next=[]
        t=0
        for x1,y1 in temp:
            x1+=1
            if 0 <= x1 < r and 0 <= y1 < c and graph[x1][y1] == ".":
                next.append((x1,y1))
            else:
                t=1
                break
        if t==1:
            for x1,y1 in temp:
                graph[x1][y1]="x"
            break
        else:
            temp=next


time=0
for i in e:
    # 왼쪽에서 지울지 오른쪽 에서 지울지 정해야 함
    de(graph, i, time % 2)
    visit = [[0] * (c) for _ in range(r)]

    # 가장 아래 행부터 해서 확인을 하도록 하자
    for j in range(c):
        if visit[r - 1][j] == 0 and graph[r - 1][j] == "x":
            bfs(r - 1, j, visit, graph)
    g1=0
    for j in range(r - 2, -1, -1):
        for k in range(c):
            if graph[j][k] == "x" and visit[j][k] == 0:
                move(j, k, graph, visit)
                g1=1
                break
        if g1==1:
            break

    time+=1

for i in graph:
    for k in i:
        print(k,end="")
    print()