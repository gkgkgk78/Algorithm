import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


#input = sys.stdin.readline

from itertools import combinations_with_replacement as cwr
from collections import Counter



def bfs(a,b):
    q=deque()
    q.append((a,b,0))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit[a][b][0]=1
    while q:
        a1,a2,a3=q.popleft()
        if a1==n-1 and a2==m-1:
            return visit[a1][a2][a3]
        for i in range(4):
            zx,zy=a1+dx[i],a2+dy[i]
            if 0<=zx<n and 0<=zy<m :
                if graph[zx][zy]==1 and a3<k:
                    if visit[zx][zy][a3+1] ==0:
                        visit[zx][zy][a3+1]=visit[a1][a2][a3]+1
                        q.append((zx,zy,a3+1))
                elif graph[zx][zy]==0 and visit[zx][zy][a3]==0:
                    visit[zx][zy][a3]=visit[a1][a2][a3]+1
                    q.append((zx,zy,a3))
    return -1
n,m,k=map(int,input().split())
visit = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
graph=[]
wall=[]
for j in range(n):
    a=list(map(int,input().rstrip()))
    graph.append(a)
aw=99999

t=bfs(0,0)

if t==-1:
    print(-1)
else:
    print(t)



