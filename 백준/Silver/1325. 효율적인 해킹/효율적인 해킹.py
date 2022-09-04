import sys,copy
from itertools import combinations

from collections import deque

input=sys.stdin.readline


def bfs(t):
    global max,ho
    visit=[0]*(n+1)
    q=deque()
    q.append(t)
    count=1
    while q:
        dd=q.popleft()
        visit[dd]=1

        for i in graph[dd]:
            if visit[i]==0:
                q.append(i)
                count=count+1
                visit[i] = 1
    if count>max:
            max=count
            ho=[]
            ho.append(t)
    elif count==max:
            ho.append(t)

    return max

max=-1
n,m=map(int,input().split())

b=m

graph=[[0] for _ in range(n+1)]

ho=[]
while b>0:
    s,t=map(int,input().split())
    graph[t].append(s)
    b=b-1

for i in range(1,n+1):
    h=bfs(i)

ho.sort()
print(*ho)




































