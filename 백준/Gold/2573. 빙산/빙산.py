import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합




from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline



def dfs(s,d):
    q=deque()
    visit[s][d]=1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q.append((s,d))
    h = deque()
    while q:
        g1,g2=q.popleft()
        visit[g1][g2]=1
        vc=0

        for i in range(0,4):
            zx=g1+dx[i]
            zy=g2+dy[i]
            if 0<=zx<r and 0<=zy<c :
                if graph[zx][zy]==0:
                    vc=vc+1
                elif graph[zx][zy]>0 and visit[zx][zy]==0:
                    q.append((zx,zy))
                    visit[zx][zy]=1
        if graph[g1][g2]-vc<=0:
            h.append((g1,g2))
        else:
            graph[g1][g2]=graph[g1][g2]-vc
    for i in range(0,len(h)):
        t1,t2=h.popleft()
        graph[t1][t2]=0



r,c=map(int,input().split())

graph=[]
for i in range(r):
    g=list(map(int,input().split()))
    graph.append(g)

year=0
count0=0

while 1:
    count0=0
    visit=[[0]*c for _ in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            if visit[i][j]==0 and graph[i][j]>0:
                dfs(i,j)
                count0=count0+1

    year=year+1

    if count0>1:
        print(year-1)
        exit(0)
    sumz=0
    for i in range(0, r):
        sumz+=sum(graph[i])
    if sumz==0:
        print(0)
        exit(0)

print(0)