import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque

sys.setrecursionlimit(10 ** 5)



input = sys.stdin.readline
a = int(input().rstrip())
graph=[[]for _ in range(a+1)]



def bfs(i,ae):
    q=deque()
    q.append((i,ae))
    visit=[0 for _ in range(a )]
    visit1 = [-1 for _ in range(a )]
    while q:
        a1,a2=q.popleft()
        visit[a1]=1
        visit1[a1]=a2
        for k in graph[a1]:
            if visit[k]==0:
                q.append((k,a2+1))
                visit[k]=1
    return visit1

while 1:
    la,lb=map(int,input().split())
    if la==-1 and lb==-1:
        break
    else:
        graph[la-1].append((lb-1))
        graph[lb-1].append((la-1))

rere=[0 for _ in range(a)]
for k in range(0,a):
    jo=bfs(k,0)
    ho=max(jo)
    rere[k]=ho
h1=min(rere)
h2=rere.count(h1)
print(h1,h2)
aa=[]
for k in range(len(rere)):
    if rere[k]==h1:
        aa.append(k+1)
print(*aa)












