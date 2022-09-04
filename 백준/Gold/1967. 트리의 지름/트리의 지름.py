import sys, copy
import heapq,math
from itertools import combinations
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

a=int(input().rstrip())

graph=[[] for _ in range(a+1)]


for i in range(a-1):
    a1,a2,a3=map(int,input().split())
    graph[a1].append([a2,a3])
    graph[a2].append([a1, a3])
total=-1
find=0
l_find=0
l_sumz=-1
visit=[-1]*10001
def dfs(start,weight):
    global total,sumz
    for i in graph[start]:
        a,b=i
        if visit[a]==-1:
            visit[a]=weight+b
            dfs(a,weight+b)
visit[1]=0
dfs(1,0)
start=visit.index(max(visit))
visit=[-1]*10001
visit[start]=0
dfs(start,0)
print(max(visit))