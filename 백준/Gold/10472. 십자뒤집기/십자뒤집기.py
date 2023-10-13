import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline


def make_char(graph):
    aa = ""
    for i in graph:
        a = "".join(i)
        aa += a
    return aa


def make_graph(now):
    graph = []
    index = 0
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(now[index])
            index += 1
        graph.append(temp)
    return graph


def check(now):
    ch = 0
    for i in now:
        if i == "*":
            return -1
    return 1


def bfs(graph):
    q = deque()
    nex = make_char(graph)
    visit = dict()
    visit[nex] = 1
    q.append((nex, 0))
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]
    while q:
        now, value = q.popleft()
        ee = check(now)
        if ee == 1:
            return value
        gra = make_graph(now)
        for i in range(3):
            for j in range(3):
                for k in range(5):
                    zx = i + dx[k]
                    zy = j + dy[k]
                    if i == 1 and j == 0:
                        j = 0
                    if 0 <= zx < 3 and 0 <= zy < 3:
                        if gra[zx][zy] == "*":
                            gra[zx][zy] = "."
                        else:
                            gra[zx][zy] = "*"
                nex = make_char(gra)
                if nex not in visit:
                    visit[nex] = 1
                    q.append((nex, value + 1))
                for k in range(5):
                    zx = i + dx[k]
                    zy = j + dy[k]
                    if 0 <= zx < 3 and 0 <= zy < 3:
                        if gra[zx][zy] == ".":
                            gra[zx][zy] = "*"
                        else:
                            gra[zx][zy] = "."


n = int(input().rstrip())
for _ in range(n):
    graph = []
    for _ in range(3):
        e = list(map(str, input().rstrip()))
        graph.append(e)
    a = bfs(graph)
    print(a)