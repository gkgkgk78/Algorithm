import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


#그래프를 둘로 분할하여서 각 집합에 속한 정점 끼리는 인접 하지 않도록 분할 하자
#이분 그래프 이다.

#이분 그래프 인지 아닌지 판별 하도록 하라


def bfs(ver,visit):
    q=deque()
    visit[ver]=1
    q.append((ver,1))
    while q:
        vertex,color=q.popleft()
        for i in graph[vertex]:
            if visit[i]==0:
                if color==1:
                    visit[i]=2
                    q.append((i, 2))
                else:
                    visit[i]=1
                    q.append((i, 1))


k=int(input().rstrip())
for _ in range(k):
    v,e=map(int,input().split())
    #정점의 개수와 간선의 개수가 주어 졌다
    visit=[0]*(v+1)
    edge=[]
    graph=[[]for _ in range(v+1)]
    for i in range(e):
        a1,a2=map(int,input().split())
        edge.append((a1,a2))
        graph[a1].append(a2)
        graph[a2].append(a1)

    for i in range(1,v+1):
        if visit[i]==0:
            bfs(i,visit)
    check=0
    for a1,a2 in edge:
        if visit[a1]==visit[a2]:
            check=1
            break
    if check==0:
        print("YES")
    else:
        print("NO")