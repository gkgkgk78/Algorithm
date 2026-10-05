from collections import deque
def solution(maps):
    answer = []
    
    
    graph=[]
    for i in maps:
        temp=[]
        for j in i:
            temp.append(j)
        graph.append(temp)
    maps=graph
            
    

    n=len(maps)
    m=len(maps[0])
    visit=[[0]*(m)for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visit[i][j]==1 or maps[i][j]=='X':
                continue
            bfs(visit,maps,i,j,answer,n,m)
    answer.sort()
    if len(answer)==0:
        return [-1]
    
    return answer


def bfs(visit,graph,x,y,answer,n,m):
    count=(int)(graph[x][y])

    visit[x][y]=1
    q=deque()
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        sx,sy=q.popleft()
        for i in range(4):
            zx=dx[i]+sx
            zy=dy[i]+sy
            if 0<=zx<n and 0<=zy<m and graph[zx][zy]!='X' and visit[zx][zy]==0:
                visit[zx][zy]=1
                q.append((zx,zy))
                count+=(int)(graph[zx][zy])
                
    answer.append(count)