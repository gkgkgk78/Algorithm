
from collections import deque

def bfs(start,graph,n):
    visit=[-1]*(n+1)
    q=deque()
    q.append((start,0))
    visit[start]=0
    while q:
        vertex,now=q.popleft()      
        for a1 in graph[vertex]:
            if visit[a1]==-1:
                visit[a1]=now+1
                q.append((a1,now+1))
    
    return visit



def solution(n, roads, sources, destination):
    answer = []
    graph=[[]for _ in range(n+1)]
    
    for i in roads:
        a1,a2=i
        graph[a1].append(a2)
        graph[a2].append(a1)
    
    
    a1=bfs(destination,graph,n)

    for i in sources:
        now=a1[i]
        answer.append(now)
    
        
    return answer