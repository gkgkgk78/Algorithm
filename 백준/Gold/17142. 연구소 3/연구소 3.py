import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))


#input = sys.stdin.readline

from itertools import combinations_with_replacement as cwr
from collections import Counter



n,m=map(int,input().split())
graph=[]
to=[]
blank=0
for i in range(n):
    e=list(map(int,input().split()))
    for j in range(len(e)):
        if e[j]==2:
            to.append((i,j))
        elif e[j]==0:
            blank+=1
    graph.append(e)
com=list(combinations(to,m))

result=[]
def bfs(o,blank):
    visit = [[0] * n for i in range(n)]
    q=deque()
    for l in o:
        a1,a2=l
        q.append((a1,a2,0))
        visit[a1][a2]=1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    temp=0
    last=0
    la=0
    while q:
        a1,a2,a3=q.popleft()
        last=max(last,a3)
        for i in range(4):
            zx=a1+dx[i]
            zy=a2+dy[i]
            if(0<=zx<n and 0<=zy<n):
                if visit[zx][zy]==0:
                    if graph[zx][zy]==0:
                        la=a3+1
                        q.append((zx,zy,a3+1))
                        visit[zx][zy] = 1
                        temp += 1
                    elif graph[zx][zy]==2:
                        q.append((zx, zy, a3+1))
                        visit[zx][zy] = 1
                    if temp==blank:
                        break

    if(temp==blank):
        result.append(la)

# 1,5  4,3 6,0
for o in com:
    bfs(o,blank)

if len(result)==0:
    print(-1)
else :
    print(min(result))


