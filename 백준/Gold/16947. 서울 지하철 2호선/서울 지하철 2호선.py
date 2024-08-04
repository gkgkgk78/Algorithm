import sys
sys.setrecursionlimit(10**6)
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

distance = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]


for _ in range(n):
    a1,a2=map(int,input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)


#dfs를 해서 사이클을 확인하는 수밖에 없겠다

visit=[0]*(n+1)

def dfs(start,vertex,depth):

    if depth>n:
        return 0
    for i in graph[vertex]:
        if depth<=2:
            if visit[i]==0:
                visit[i]=1
                ne=dfs(start,i,depth+1)
                if ne==1:
                    return 1
                else:
                    visit[i]=0
        else:
            if i == start:
                if depth >= 3:
                    visit[i] = 1
                    return 1
            if visit[i] == 0:
                visit[i] = 1
                ne = dfs(start, i, depth + 1)
                if ne == 1:
                    return 1
                else:
                    visit[i] = 0
    return 0

for i in range(1,n+1):
    visit[i]=1
    result=dfs(i,i,1)
    if result==1:
        break
    visit[i]=0

q=deque()
for i in range(1,len(visit)):
    if visit[i]==1:
        distance[i]=-1
        q.append(i)
while q:
    a1=q.popleft()
    next=distance[a1]
    if next==-1:
        next=0
    for i in graph[a1]:
        if distance[i]==-1:
            continue
        if distance[i]==0:
            distance[i]=next+1
            q.append(i)

for i in range(1,len(distance)):
    if distance[i]==-1:
        distance[i]=0
print(*distance[1:])