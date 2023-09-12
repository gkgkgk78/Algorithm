import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

graph = []
for _ in range(5):
    e = list(map(str, input().rstrip()))
    graph.append(e)

total = []
for i in range(5):
    for j in range(5):
        total.append((i, j))



nex=list(combinations(total,7))

ans=0

def bfs(li):
    global ans

    visit=[[-1]*5 for _ in range(5)]

    for i in li:
        a1,a2=i
        visit[a1][a2]=1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    q=deque()
    q.append((li[0][0],li[0][1]))
    visit[li[0][0]][li[0][1]] = 0
    cu=1
    while q:
        a1,a2=q.popleft()
        for i in range(4):
            zx=dx[i]+a1
            zy=dy[i]+a2
            if 0<=zx<5 and 0<=zy<5 and visit[zx][zy]==1:
                q.append((zx,zy))
                visit[zx][zy]=0
                cu += 1

    if cu==7:
        ans+=1

for i in nex:
    check=0
    for a1,a2 in i:
        if graph[a1][a2]=="S":
            check+=1
    if check>=4:
        bfs(i)

print(ans)