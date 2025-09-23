from collections import deque
def bfs(vertex,visit,graph):
    q=deque()
    visit[vertex]=1
    q.append(vertex)
    while q:
        now=q.popleft()
        temp=graph[now]
        for i in range(len(temp)):
            if temp[i]==0:
                continue
            if visit[i]==0:
                visit[i]=1
                q.append(i)

def solution(n, computers):
    answer = 0    
    visit=[0]*n
    for i in range(n):
        if visit[i]==0:
            answer+=1
            bfs(i,visit,computers)
    
    return answer