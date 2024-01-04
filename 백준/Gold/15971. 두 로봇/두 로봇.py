import sys
from collections import deque

input = sys.stdin.readline

n,l,r=map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(n-1):
    a1,a2,a3=map(int,input().split())
    graph[a1].append((a2,a3))
    graph[a2].append((a1,a3))

answer=sys.maxsize
visit=[sys.maxsize]*(n+1)
def bfs(start):
    global answer
    q=deque()
    q.append((start,0,0))
    visit[start]=0
    while q:
        now,total,value=q.popleft()
        if now==r:
            answer=min(answer,total-value)
            return
        for ver,val in graph[now]:
            temp=val+visit[now]
            if visit[ver]>temp:
                visit[ver]=temp
                q.append((ver,temp,max(value,val)))

bfs(l)
print(answer)