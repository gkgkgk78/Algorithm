import sys
from collections import deque
import math
#sys.stdin = open("input.txt")
input=sys.stdin.readline

def dfs(t):
    visit_list[t]=1
    print(t,end=" ")
    for i in range(1,n+1):
        if graph[t][i]==1 and visit_list[i]==0:
            dfs(i)


def bfs(t1,t2):
    q=deque([])

    q.append((t1,t2))
    check[0][0]=1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while q:

        (g1,g2)=q.popleft()
        if visit_list2[g1][g2]==0:
            visit_list2[g1][g2]=1

            for i in range (0,4):
                nx,ny=g1+dx[i],dy[i]+g2
                if 0<=nx<n and 0<=ny<m and visit_list2[nx][ny]==0 and graph[nx][ny]==1:
                    q.append((nx,ny))
                    check[nx][ny]=check[g1][g2]+1


    print(check[-1][-1])




n,m = map(int,input().split())

graph = [ [0] * (m ) for _ in range(n) ]
visit_list = [0] * (n + 1)
visit_list2 = [ [0] * (m ) for _ in range(n) ]
check = [ [0] * (m ) for _ in range(n) ]
for i in range(0,n):
    g=list(map(int,input().rstrip()))
    for j in range (0,m):
        if g[j]==1:
            graph[i][j]=1

bfs(0,0)







