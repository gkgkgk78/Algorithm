import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10**5)



def dfs(v):
    ok=0
    q=deque()
    q.append(v)
    visit[v]=1
    while q:
        g=q.popleft()
        if visit[g] == 1:
            ok = -1
        elif visit[g]==-1:
            ok = 1

        for i in graph[g]:
            if visit[i]==0:
                q.append(i)
                visit[i]=ok
            else:
                
                    if visit[i]==-1:
                        if visit[g]==-1:
                            return 0
                    elif visit[i]==1:
                        if visit[g]==1:
                            return 0


    return 1


h=int(input())
gg=h
while gg>0:
    vertex,edge=map(int,input().split())
    graph = [[] for _ in range(0, vertex+ 1)]
    visit = [0] * (vertex + 1)
    for i in range(edge):
        t1,t2=map(int,input().split())
        graph[t1].append(t2)
        graph[t2].append(t1)


    jk=0
    for k in range (1,vertex+1):
        if visit[k]==0:
            jk=dfs(k)
        if jk==0:
            print("NO")
            break
    if jk==1:
        print("YES")



    gg=gg-1













