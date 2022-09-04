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


def bfs(t):
    q=deque([])

    q.append(v)

    while q:
        x=q.popleft()
        if visit_list2[x]==0:
            visit_list2[x]=1
            print(x,end=" ")
            for i in range (1,n+1):
                if graph[x][i]==1 and visit_list2[i]==0:
                    q.append(i)





n,m,v = map(int,input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for i in range(0,m):
    t1,t2=map(int,input().split())
    graph[t1][t2]=1
    graph[t2][t1]=1

dfs(v)
print()
bfs(v)

