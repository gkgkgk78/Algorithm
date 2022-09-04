import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

n=int(input().rstrip())
graph=list(list(map(int,input().split())) for _ in range(n))

sum=0
k=2
for i in range(1,n):
    for j in range(k):
        if j==0:
            graph[i][j]+=graph[i-1][0]
        elif j==k-1:
            graph[i][j] += graph[i - 1][j-1]
        else:
            graph[i][j]+=max(graph[i-1][j-1],graph[i-1][j])
    k+=1
print(max(graph[n-1]))
