import sys, copy
import heapq,math
from itertools import combinations
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
a=int(input().rstrip())
ss=0
graph=[[] for _ in range(a+1)]
for i in range(a):
    t=list(map(int,input().split()))
    if i==0:
        ss=t[0]
    for j in range(1,len(t)-2,2):
        graph[t[0]].append([t[j], t[j+1]])

visit=[-1]*(a+1)
def dfs (start,weight):
    for i in graph[start]:
        a1,a2=i
        if visit[a1]==-1:
            visit[a1]=weight+a2
            dfs(a1,weight+a2)
visit[ss]=0
dfs(ss,0)
start=visit.index(max(visit))
visit=[-1]*(a+1)
visit[start]=0
dfs(start,0)
print(max(visit))
