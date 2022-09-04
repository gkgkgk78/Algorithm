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
def bfs(x,y):
    q=deque()
    q.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    hie=[]
    while q:
        a1,a2=q.popleft()
        hie.append((a1,a2))
        visit[a1][a2]=1
        for i in range(4):
            tx=a1+dx[i]
            ty=a2+dy[i]
            if 0<=tx<n and 0<=ty<m and graph[tx][ty]==0:
                if visit[tx][ty]==0:
                    q.append((tx,ty))
                    visit[tx][ty]=1
    return hie



n,m=map(int,input().split())
graph=[]
to=[]
fin=dict()
visit=[[0 for _ in range(m)]for _ in range(n) ]
wall=[]
for i in range(n):

    e=list(map(int,input().rstrip()))

    for j in range(len(e)):
        if(e[j]==0):
            to.append((i,j))
        else:
            wall.append((i,j))
    graph.append(e)

ti=2
for a1,a2 in to:
    if(visit[a1][a2]==0):
        jj=bfs(a1,a2)
        fin[ti]=len(jj)

        for y1,y2 in jj:
            graph[y1][y2]=ti
        ti = ti + 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit=[[0 for _ in range(m)]for _ in range(n) ]
for a1,a2 in wall:
    su=0
    vi=[]
    for i in range(4):
        tx = a1 + dx[i]
        ty = a2 + dy[i]
        if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] != 1:
            if graph[tx][ty]not in vi:
                su+=fin[graph[tx][ty]]
                vi.append(graph[tx][ty])
    visit[a1][a2]=su+1

for i in range(n):
    for j in range(len(visit[i])):
        print(visit[i][j]%10,end="")
    print()