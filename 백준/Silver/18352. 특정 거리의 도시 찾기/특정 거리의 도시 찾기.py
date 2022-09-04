import sys, copy,heapq
import heapq,math
from itertools import permutations
from collections import deque
sys.setrecursionlimit(10**9)

# input = sys.stdin.readline

input=sys.stdin.readline


#c는 최단거리 d는 시작 점
a,b,c,d=map(int,input().split())
graph=[[] for i in range(a+1)]
for i in range(b):
    a1,a2=map(int,input().split())
    graph[a1].append(a2)

visit=[0] * (a+1)
distance=[0]*(a+1)
def bfs():
    q=deque()
    q.append(d)
    visit[d]=1
    while q:
        t1=q.popleft()

        for i in graph[t1]:
            if visit[i]==0:
                distance[i]+=distance[t1]+1
                visit[i] = 1
                q.append(i)

bfs()

if  c not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i]==c:
            print(i)



