import sys
from collections import deque

input = sys.stdin.readline
t=int(input().rstrip())

def bfs(vertex,what,color,visit,graph):

    visit[vertex]=1
    q=deque()
    color[vertex]=0
    q.append(vertex)
    while q:
        a1=q.popleft()
        ne=-1
        if color[a1]==0:
            ne=1
        else:
            ne=0
        for i in graph[a1]:
            if visit[i]==0:
                visit[i]=1
                color[i]=ne
                q.append(i)



for _ in range(t):
    v,e=map(int,input().split())
    graph=[[]for _ in range(v+1)]
    visit=[0]*(v+1)
    total=[]
    for _ in range(e):
        a1,a2=map(int,input().split())
        graph[a1].append(a2)
        graph[a2].append(a1)
        total.append((a1,a2))
    color=[-1]*(v+1)
    for i in range(1,v+1):
        if visit[i]==0:
            bfs(i,0,color,visit,graph)
    tt=0
    for a1,a2 in total:
        if color[a1]==color[a2]:
            tt=1
            break
    if tt==0:
        print("YES")
    else:
        print("NO")