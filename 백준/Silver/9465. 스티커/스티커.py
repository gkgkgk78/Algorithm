import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

n=int(input().rstrip())

for i in range(n):
    n1=int(input().rstrip())
    graph=list(list(map(int,input().split())) for _ in range(2))

    for j in range(1,n1):
        if j == 1:
            graph[0][j] += (graph[1][j - 1])
            graph[1][j] += (graph[0][j - 1])
        else:
            graph[0][j]+=max(graph[1][j-2],graph[1][j-1])
            graph[1][j]+=max(graph[0][j-2],graph[0][j-1])

    print(max(graph[0][n1 - 1], graph[1][n1 - 1]))







