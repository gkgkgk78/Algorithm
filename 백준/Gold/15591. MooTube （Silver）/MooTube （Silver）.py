import sys
from collections import deque
input = sys.stdin.readline

n,q=map(int,input().split())

total=[[sys.maxsize]*(n+1) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a1,a2,a3=map(int,input().split())
    graph[a1].append((a2,a3))
    graph[a2].append((a1, a3))

#이제 탐색을 진행 해보도록 하자


def bfs(vertex):
    global total
    q=deque()
    q.append(vertex)
    visit=[0]*(n+1)
    visit[vertex]=1
    aa=total
    while q:
        now=q.popleft()
        for i in graph[now]:
            a1,a2=i
            if visit[a1]==0:
                total[vertex][a1]=min(a2,total[vertex][now])
                visit[a1]=1
                q.append(a1)




for i in range(1,n+1):
    bfs(i)

for l in range(q):
    a1,a2=map(int,input().split())
    temp=0
    for l in total[a2]:
        if l>=a1 and l !=sys.maxsize:
            temp+=1
    print(temp)