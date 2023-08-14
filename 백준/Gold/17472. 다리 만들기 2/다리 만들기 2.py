import sys
from collections import deque
input=sys.stdin.readline


n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))


visit=[[0]*(m)for _ in range(n)]
#이제 그래프에 있는 것들 이름을 지어줄거아ㅣㅁ
count=1

def bfs(x,y,count):
    q=deque()
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            zx=dx[i]+x
            zy=dy[i]+y
            if 0<=zx<n and 0<=zy<m:
                if visit[zx][zy]==0 and graph[zx][zy]==1:
                    visit[zx][zy]=1
                    q.append((zx,zy))
                    graph[zx][zy]=count


for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visit[i][j]==0:
            visit[i][j]=1
            bfs(i,j,count)
            graph[i][j]=count
            count+=1

#이제 union find 를 해야 하니 해보도록 하자
parents=[0]*(count+1)
def make():
    for i in range(1,count+1):
        parents[i]=i
make()
def find(x):
    if parents[x]==x:
        return x
    parents[x]=find(parents[x])
    return parents[x]
def union(a1,a2):
    z1=find(a1)
    z2=find(a2)
    if z1==z2:
        return 0
    if z1<z2:
        parents[z2]=z1
    else:
        parents[z1]=z2

def dfs(x,y,dir):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    zx=x
    zy=y
    co=0
    if x==1 and y==6 and dir==2:
        dir=2
    while 1:
        zx+=dx[dir]
        zy+=dy[dir]
        if 0<=zx<n and 0<=zy<m:
            if graph[zx][zy]!=0:
                h1=find(graph[zx][zy])
                h2=find(graph[x][y])
                if h1==h2:
                    return -1
                else:
                    return co

        else:
            return -1
        co += 1

    return -1


def dfs1(x, y, dir):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    zx = x
    zy = y

    while 1:
        zx += dx[dir]
        zy += dy[dir]
        if 0 <= zx < n and 0 <= zy < m:
            if graph[zx][zy] != 0:
                union(graph[zx][zy], graph[x][y])
                return


ans = 0
while 1:
    # 이제 탐색을 시작 하도록 하지
    total = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                for k in range(4):
                    h = dfs(i, j, k)
                    if h != -1 and h >= 2:
                        total.append((i, j, k, h))

    # 가장 짧은것 부터 증가를 시키도록 하자
    total = sorted(total, key=lambda x: x[3])

    if len(total) == 0:
        break
    z1, z2, z3, z4 = total[0]

    dfs1(z1, z2, z3)
    ans += z4

for i in range(1,count+1):
    parents[i]=find(i)
z1=parents[1]
for i in range(2,count):
    if parents[i]!=z1:
        ans=0
        break

if ans == 0:
    print(-1)
else:
    print(ans)