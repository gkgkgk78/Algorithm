import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math
a,b=map(int,input().split())
graph=[[0]*(b+1) for _ in range(a+1)]
toys=[list(map(int,input().split())) for _ in range(a)]
for i in range(1,a+1):
    for j in range(1,b+1):
        w=toys[i-1][0]
        v=toys[i-1][1]

        if j<w:
            graph[i][j]=graph[i-1][j]
        else:
            graph[i][j]=max(graph[i-1][j-w]+v,graph[i-1][j])
print(graph[a][b])
