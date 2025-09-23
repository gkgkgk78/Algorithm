import heapq
def bfs(n,m,visit,graph):
    q=[]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    visit[0][0]=1
    heapq.heappush(q,[1,0,0])#거리, x,y
    while q:
        dis,x,y=heapq.heappop(q)
        if x==n-1 and y==m-1:
            return dis
        for i in range(4):
            zx=dx[i]+x
            zy=dy[i]+y
            if 0<=zx<n and 0<=zy<m and graph[zx][zy]==1 and visit[zx][zy]==0:
                visit[zx][zy]=1
                heapq.heappush(q,[(dis+1),zx,zy])
    print(visit)
    return -1
    


def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    visit=[ [0]*(m)for _ in range(n)]
    return bfs(n,m,visit,maps)
    
    
