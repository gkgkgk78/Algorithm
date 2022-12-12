import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
n=2**n
graph=[list(map(int,input().split())) for _ in range(n)]
level=list(map(int,input().split()))
def bfs(graph,isin):
    x=0
    y=0
    visit = [[0 for _ in range(n)] for _ in range(n)]
    ans=0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for a1,a2 in isin:
        if visit[a1][a2]==0 :
            temp=0
            q=deque()
            q.append((a1,a2))
            while q:
                z1,z2=q.popleft()
                visit[z1][z2]=1
                temp+=1
                for i in range(4):
                    zx=z1+dx[i]
                    zy=z2+dy[i]
                    if 0<=zx<n and 0<=zy<n and graph[zx][zy]>0 and visit[zx][zy]==0:
                        visit[zx][zy]=1
                        q.append((zx,zy))
            ans=max(ans,temp)

    return ans

def rotate(graph,startx,starty,now):
    #시계방향으로 90도를 회전을 하면은 된다.
    temp=[[0 for _ in range(now)] for _ in range(now)]
    sx=0
    sy=0
    cy=starty
    for z in range(now):
        for l in range(startx+now-1,startx-1,-1):
            temp[sx][sy]=graph[l][cy]
            sy+=1
        cy+=1
        sy=0
        sx+=1
    sx = 0
    sy = 0
    for x in range(startx,startx+now):
        for y in range(starty,starty+now):
            graph[x][y]=temp[sx][sy]
            sy+=1
        sx+=1
        sy=0
    return graph

#회전을 위한 부분
for i in level:
    if(i>0):
        now=2**i
        startx=0
        starty=0
        while startx<n:
            while starty<n:
                graph=rotate(graph,startx,starty,now)
                starty+=now
            startx+=now
            starty=0
    #회전을 시키고 난후에

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    deleted=[]
    for x in range(0,n):
        for y in range(0,n):
            if graph[x][y]>0:
                #얼음이 있는 칸 3개 또는 그 이상과 인접해 있지 않은 칸은 얼음의 양이 1줄어듬
                temp_check=0
                for l in range(4):
                    zx=x+dx[l]
                    zy=y+dy[l]
                    if 0<=zx<n and 0<=zy<n:
                        if graph[zx][zy]==0:
                            temp_check+=1
                    else:
                        temp_check+=1
                if temp_check>=2:
                    deleted.append((x,y))
    for a1,a2 in deleted:
        graph[a1][a2]-=1
answer=0
isin=[]

for i in range(0,n):
    for j in range(0,n):
        answer+=graph[i][j]
        if graph[i][j]>0:
            isin.append((i,j))

print(answer)
print(bfs(graph,isin))