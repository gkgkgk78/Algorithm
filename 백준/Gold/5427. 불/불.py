import sys
from collections import deque
input = sys.stdin.readline

t=int(input().rstrip())
for _ in range(t):
    m,n=map(int,input().split())
    graph=[]
    fire=deque()
    user=deque()
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        e=list(map(str,input().rstrip()))
        for j in range(m):
            if e[j]=="@":
                user.append((i,j))
                e[j]="."
                visit[i][j]=1
            elif e[j]=="*":
                fire.append((i,j))
        graph.append(e)
    time=0

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    while 1:
        if len(user)==0:
            break
        temp_fire=deque()
        while fire:
            a1,a2=fire.popleft()
            for i in range(4):
                zx=a1+dx[i]
                zy=a2+dy[i]
                if 0<=zx<n and 0<=zy<m:
                    if graph[zx][zy]==".":
                        graph[zx][zy]="*"
                        temp_fire.append((zx,zy))
        fire=temp_fire
        t=0
        temp_user=deque()
        while user:
            a1,a2=user.popleft()
            for i in range(4):
                zx = a1 + dx[i]
                zy = a2 + dy[i]
                if 0 <= zx < n and 0 <= zy < m:
                    if visit[zx][zy]==0 and graph[zx][zy] == ".":
                        visit[zx][zy]=1
                        temp_user.append((zx,zy))
                else:
                    t=1
                    break
        user=temp_user
        time+=1
        if t==1:
            break

    if t==0:
        print("IMPOSSIBLE")
    else:
        print(time)