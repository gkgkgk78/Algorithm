import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

a=int(input().rstrip())
result=[]
for i in range(a):
    q=int(input().rstrip())

    mins=[]
    maxs=[]
    visit=[0]*q
    for j in range(q):
        a1, a2 = map(str, input().split())
        a2=int(a2)
        if a1=="I":
                heapq.heappush(mins,(a2,j))
                heapq.heappush(maxs, (-a2,j))
                visit[j]=1
        else :
            if a2==-1 :
                while mins and not visit[mins[0][1]]:
                    heapq.heappop(mins)
                if mins:
                    visit[mins[0][1]]=0
                    heapq.heappop(mins)
            else:
                while maxs and not visit[maxs[0][1]]:
                    heapq.heappop(maxs)
                if maxs:
                    visit[maxs[0][1]] = 0
                    heapq.heappop(maxs)

    while mins and not visit[mins[0][1]]:
        heapq.heappop(mins)
    while maxs and not visit[maxs[0][1]]:
        heapq.heappop(maxs)

    result.append(f'{-maxs[0][0]} {mins[0][0]}' if maxs and mins else 'EMPTY')

for i in range(len(result)):
    print(result[i])
