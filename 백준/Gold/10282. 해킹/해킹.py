import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합




from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline

n=int(input().rstrip())


def dik(s):
    q=[]

    distance[s]=0
    heapq.heappush(q,(0,s))

    while q:
        dis,now=heapq.heappop(q)
        if distance[now]<dis:
            continue
        for i in graph[now]:
            cost=dis+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

for _ in range(n):
    n,d,c=map(int,input().split())
    graph=[[]for _ in range(n+1)]
    distance=[10**7 ]*(n+1)


    for _ in range(d):
        a1,a2,a3=map(int,input().split())
        graph[a2].append((a1,a3))
    count=0
    uiui=-10
    dik(c)

    for o in range(1,n+1):
        if(distance[o]!=10**7):
            count+=1
            uiui=max(uiui,distance[o])
    print(count,uiui)