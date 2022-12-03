import sys
from collections import deque
input=sys.stdin.readline
def dfs1(s1,s2,c):
    q=deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q.append((s1,s2))
    while q:
        (v1,v2)=q.popleft()
        for i in range(0,4):
            sx=dx[i]+v1
            sy=dy[i]+v2

            if 0<=sx<n and 0<=sy<n and visit[sx][sy]==0 and graph[sx][sy]==1:
                visit[sx][sy]=1
                graph[sx][sy]=c
                q.append((sx,sy))
def dfs(s):
    global  mins
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q=deque()

    visit = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]==s:

                q.append((i,j))
                visit[i][j]=0

    while q:
        (v1,v2)=q.popleft()

        for i in range(0,4):
            sx=dx[i]+v1
            sy=dy[i]+v2

            if 0<=sx<n and 0<=sy<n :
                if graph[sx][sy]!=0 and graph[sx][sy]!=s:

                    mins=min(mins,visit[v1][v2])
                    return
                if graph[sx][sy]==0 and visit[sx][sy]==-1:
                    visit[sx][sy]=visit[v1][v2]+1
                    q.append((sx,sy))
n=int(input())
graph=[]
visit=[[0]*n for _ in range(n)]
for i in range(0,n):
    g=list(map(int,input().split()))
    graph.append(g)
count=1
for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and graph[i][j]==1:
            graph[i][j]=count
            dfs1(i,j,count)
            count=count+1
q=deque()
mins=999999
for i in range(1,count):
    dfs(i)
print(mins)