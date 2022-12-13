import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

#이동 방향을 의미를 함
dir=[(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
da=[(-1,-1),(-1,1),(1,-1),(1,1)]
def dodo(z):
    # 오른쪽 증가시에는 % 한후 더한후에 %해주면 나옴
    # 왼쪽으로 증가시에는 %한후 더한후에 <0 이라면 n-절댓값() 하면됨
    if z<0 or z>=n:
        if z>=n:
            return z%n
        else:
            return n-abs(z)
    else:
        return z
gr=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
visit=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a1,a2=map(int,input().split())
    dirx=dir[a1][0]
    diry=dir[a1][1]
    #단계1
    #모든 구름이 di방향으로 이동을 해야함
    temp=[]
    for i in gr:
        t1,t2=i
        t1+=(dirx*a2)%n
        t2+=(diry*a2)%n
        t1=dodo(t1)
        t2=dodo(t2)
        graph[t1][t2] += 1
        temp.append((t1,t2))
        visit[t1][t2]=1

    #물복사 버그 마법을 시전 하고자 한다.+
    for l1,l2 in temp:
        count=0
        for i1,i2 in da:
            zx=l1+i1
            zy=l2+i2
            if 0<=zx<n and 0<=zy<n and graph[zx][zy]>0:
                count+=1
        graph[l1][l2]+=count
    gr=[]
    for i in range(n):
        for j  in range(n):
            if graph[i][j]>=2 and visit[i][j]==0:
                graph[i][j]-=2
                gr.append((i,j))
    for i,j in temp:
        visit[i][j]=0

ans=0
for i in graph:
    ans+=sum(i)

print(ans)