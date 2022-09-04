import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations
from collections import deque
sys.setrecursionlimit(10**9)

# input = sys.stdin.readline

input=sys.stdin.readline


a,b=map(int,input().split())
graph=[]
#0은 빈칸 1은 벽, 2는 바이러스가 있는곳
blank=[]
virus=[]
for i in range(a):
    d=list(map(int,input().split()))
    for j in range(len(d)):
        if d[j]==0:
            blank.append((i,j))
        elif d[j]==2:
            virus.append((i,j))
    graph.append(d)

g=list(combinations(blank,3))


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    li=[]
    while q:
        z1,z2=q.popleft()
        for i in range(4):
            zx=z1+dx[i]
            zy=z2+dy[i]
            if 0<=zx<a and  0<=zy<b :
                if graph[zx][zy]==0:
                    graph[zx][zy]=2
                    q.append((zx,zy))
                    li.append((zx,zy))
    return li
maxs=-1
for i in g:

    q=deque()
    for j in i:
        z1,z2=j
        graph[z1][z2]=1
    for k in virus:
        t1,t2=k
        q.append((t1,t2))
    li=bfs()
    sumz = 0
    for h in range(a):
        for j in range(b):
            if graph[h][j] == 0:
                sumz += 1
    maxs=max(maxs,sumz)
    for k in li:
        z1,z2=k
        graph[z1][z2]=0
    for j in i:
        z1,z2=j
        graph[z1][z2]=0
print(maxs)