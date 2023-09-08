import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
graph = [[] for _ in range(n + 1)]
graph1 = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph1[a2].append(a1)

ans = 0



def bfs(ver, graph):
    visit = [0] * (n + 1)
    visit[ver] = 1
    q = deque()
    q.append(ver)
    while q:
        a1 = q.popleft()
        for i in graph[a1]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1


    return visit


for i in range(1, n + 1):
    z1 = bfs(i, graph)
    z2 = bfs(i, graph1)
    cn=0
    for j in range(1,n+1):
        if z1[j]==0 and z2[j]==0:
            cn+=1
    print(cn)