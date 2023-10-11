import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
total = dict()
ans=0
for _ in range(n):
    e = list(map(str, input().split()))
    if e[0] == "1":
        if e[1] not in total:
            total[e[1]] = []
        ne = e[3:]
        for i in ne:
            total[e[1]].append(-(int)(i))
    else:
        if e[1] not in total:
            continue
        now=total[e[1]]
        if len(now)<=(int)(e[2]):
            ans+=sum(now)*-1
            total[e[1]]=[]
        else:
            heapq.heapify(now)
            for i in range((int)(e[2])):
                ans-=heapq.heappop(now)
            total[e[1]] = now
print(ans)