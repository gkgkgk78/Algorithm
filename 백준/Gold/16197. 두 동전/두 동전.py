import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
coin=[]

for i in range(n):
    e=list(map(str,input().rstrip()))
    for j in range(m):
        if e[j]=="o":
            coin.append((i,j,1))
            #visit[i][j]=1
    graph.append(e)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

answer=sys.maxsize


def dfs(graph,count,coin):
    global answer
    if count>10:
        return
    check=0
    for l in range(2):
        a1,a2,a3=coin[l]
        if a3==0:#죽은거 개수를 셈
            check+=1
    if check==1:
        answer=min(answer,count)
        return
    elif check==2:
        return

    for i in range(4):
        cou=2
        coinz=[]
        for l in range(2):
            a1,a2,a3=coin[l]
            zx=a1+dx[i]
            zy=a2+dy[i]
            if zx < 0 or zx >= n or zy < 0 or zy >= m:
                a3 = 0
            else:
                if graph[zx][zy]=="#":
                    zx=a1
                    zy=a2

            coinz.append((zx,zy,a3))
        dfs(graph,count+1,coinz)

dfs(graph,0,coin)

if answer!=sys.maxsize:
    print(answer)
else:
    print(-1)