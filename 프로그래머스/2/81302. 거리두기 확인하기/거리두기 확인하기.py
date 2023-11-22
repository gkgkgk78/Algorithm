from collections import deque


def bfs(graph,x,y):
    q=deque()
    n=len(graph)
    m=len(graph[0])
    visit=[[0]*(m)for _ in range(n)]
    visit[x][y]=1
    q.append((x,y,0))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y,now=q.popleft()
        if now>=2:
            continue
        for i in range(4):
            zx=x+dx[i]
            zy=y+dy[i]
            if 0<=zx<n and 0<=zy<m and graph[zx][zy]!="X":
                if visit[zx][zy]==0:
                    if graph[zx][zy]=="P":
                        return -1
                    visit[zx][zy]=1
                    q.append((zx,zy,now+1))
    
    
    return 1
    


def solution(places):
    answer = []
    graph=[]
    for i in places:
        graph=[]
        for j in i:
            e=list(map(str,j.rstrip()))
            graph.append(e)
        n=len(graph)
        m=len(graph[0])
        ee=0
        for i1 in range(n):
            for i2 in range(m):
                if graph[i1][i2]=="P":
                    t2=bfs(graph,i1,i2)
                    if t2==-1:
                        ee=1
                        break
            if ee==1:
                break
        if ee==0:
            answer.append(1)
        else:
            answer.append(0)
    
    
    
    
    return answer