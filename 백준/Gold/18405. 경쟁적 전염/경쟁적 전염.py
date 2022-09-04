import sys, copy
import heapq,math
from itertools import combinations,permutations
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
import functools,operator
n,k=map(int,input().split())
data=[]
def bfs():

    while q:
        s1, s2, s3, s4 = q.popleft()
        if s2 == x1:
            break
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        for i in range(4):
            tx=dx[i]+s3
            ty=dy[i]+s4
            if 0<=tx<n and 0<=ty<n:
                if graph[tx][ty]==0:
                    graph[tx][ty]=s1
                    q.append((s1,s2+1,tx,ty))

graph=[]
state=list([]for _ in range(k+1))
for i in range(n):
    g=list(map(int,input().split()))
    for j in range(len(g)):
        if g[j]>0:
            data.append((g[j],0,i,j))
    graph.append(g)
data.sort()
x1,x2,x3=map(int,input().split())
q=deque(data)
time=0
bfs()
print(graph[x2 - 1][x3 - 1])
