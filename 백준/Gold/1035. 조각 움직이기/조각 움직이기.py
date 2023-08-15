import sys
from collections import deque

input = sys.stdin.readline
visit = dict()

first = ""
graph = []
for _ in range(5):
    e = list(map(str, input().rstrip()))
    graph.append(e)
    for j in e:
        first += j


def find(graph):
    zx = 0
    zy = 0
    c = 0
    total = []
    temp = []
    count = 0
    fx = -1
    fy = -1
    for i in graph:
        if i == "*":
            count += 1
        temp.append(i)
        c += 1
        zx += 1
        if c == 5:
            c = 0
            total.append(temp)
            temp = []
    for i in range(5):
        for j in range(5):
            if total[i][j] == "*":
                fx = i
                fy = j
                break
    # 이제 시작 할거임

    visit = [[0] * (5) for _ in range(5)]
    visit[fx][fy] = 1

    q = deque()
    q.append((fx, fy))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ff = 0
    while q:
        a1, a2 = q.popleft()
        ff += 1
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < 5 and 0 <= zy < 5:
                if visit[zx][zy] == 0 and total[zx][zy] == "*":
                    visit[zx][zy] = 1
                    q.append((zx, zy))
    if ff == count:
        return 1
    else:
        return -1


def make(graph):
    zx = 0
    zy = 0
    c = 0
    total = []
    temp = []
    count = 0
    for i in graph:
        temp.append(i)
        c += 1
        zx += 1
        if c == 5:
            c = 0
            total.append(temp)
            temp = []
    return total


def bfs():
    q = deque()
    # 이제 시작을 해보도록 하자
    visit[first] = 1
    q.append((first, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        gr, count = q.popleft()

        # 우선 모두다 연결이 되어 있는지 확인 하는게 필요하다
        ee = find(gr)
        if ee == 1:
            print(count)
            return
        now = make(gr)
        # 이제 그래프로 만들 었음

        for i in range(5):
            for j in range(5):
                if now[i][j] == "*":
                    for k in range(4):
                        zx = i + dx[k]
                        zy = j + dy[k]
                        if 0 <= zx < 5 and 0 <= zy < 5:
                            if now[zx][zy] == ".":
                                now[zx][zy] = "*"
                                now[i][j] = "."
                                temp = ""
                                for i1 in range(5):
                                    for j1 in range(5):
                                        temp += now[i1][j1]
                                if temp not in visit:
                                    visit[temp] = 1
                                    q.append((temp, count + 1))
                                now[zx][zy] = "."
                                now[i][j] = "*"

bfs()