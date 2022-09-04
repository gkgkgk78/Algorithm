import sys, copy, heapq
import heapq, math
from queue import PriorityQueue
from itertools import permutations, combinations, product
from collections import deque
from itertools import product

#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline





def prim():
    global result
    count = 0
    q = []
    heapq.heappush(q, (0, 0))
    while len(q) > 0:
        a1, a2 = heapq.heappop(q)  # 거리 인덱스
        if (visit[a2] == 1):
            continue
        visit[a2] = 1
        count += 1
        if (count == n):
            break
        for a3, a4 in graph[a2]:
            if (visit[a3] == 0 and dist[a3] > a4):
                dist[a3] = a4
                heapq.heappush(q, (dist[a3], a3))
lo=[]
while(1):
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    graph=[[] for _ in range(n)]
    visit=[0 for _ in range(n)]
    dist=[0 for _ in range(n)]
    for i in range(n):
        dist[i]=math.inf
    total=0
    ex=0
    for _ in range(m):
        t=list(map(int,input().split()))

        a1=t[0]
        a2 = t[1]
        a3 = t[2]
        graph[a1].append((a2,a3))
        graph[a2].append((a1,a3))
        total+=a3

    dist[0]=0
    result=0

    prim()
    for i in dist:
        result+=i
    y=total-result
    lo.append(y)
for i in lo:
    print(i)