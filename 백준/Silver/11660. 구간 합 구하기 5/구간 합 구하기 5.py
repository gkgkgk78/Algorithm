import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

graph=[]
n,m=map(int,input().split())
sums=[[0]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
    sums[i][0]=graph[i][0]
    for j in range(1,n):
        sums[i][j]=sums[i][j-1]+graph[i][j]

for i in range(m):
    t=list(map(int,input().split()))
    x1=t[0]-1
    y1 = t[1] - 1
    x2 = t[2] - 1
    y2 = t[3] - 1
    sumz=0
    if x1==x2 and y1==y2:
        print(graph[x1][y1])
    else:
        for i in range(x1,x2+1):
            if y1!=0:

                sumz+=(sums[i][y2]-sums[i][y1-1])
            else:
                sumz+=sums[i][y2]

        print(sumz)
