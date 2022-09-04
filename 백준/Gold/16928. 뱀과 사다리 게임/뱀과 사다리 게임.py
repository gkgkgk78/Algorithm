import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math
n,m=map(int,input().split())
visit=[-1]*101
stair=[-1]*101
for i in range(n+m):
    a1,a2=map(int,input().split())
    stair[a1]=a2
def bfs():
    global visit,stair
    while q:
        gg = q.pop()
        if stair[gg] != -1:
            go = stair[gg]
            if visit[go] != -1:
                visit[go] = min(visit[go], visit[gg])
            else:
                visit[go] = visit[gg]
            q.append(go)
        else:
            for i in range(1,7):
                    xx=gg+i
                    if xx>100:
                        continue
                    else:
                        if visit[xx]>visit[gg]+1 or visit[xx]==-1:
                            q.append(xx)
                            visit[xx]=visit[gg]+1
q=deque()
q.append(1)
visit[1]=0
bfs()
print(visit[100])