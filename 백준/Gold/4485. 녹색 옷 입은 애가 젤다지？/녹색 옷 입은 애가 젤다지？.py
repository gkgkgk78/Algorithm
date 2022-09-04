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

count=1
def dd():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))#가중치 갈곳의 위치
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[0][0] = 0
    while q:
        dis, x,y = heapq.heappop(q)
        if x==n-1 and y==n-1:
            print(f'Problem {count}: {visit[n-1][n-1]}')

        for i in range(4):
            zx=dx[i]+x
            zy=dy[i]+y
            if 0<=zx<n and 0<=zy<n:
                if visit[zx][zy] < dis:
                    continue
                else:
                        cost = dis + graph[zx][zy]
                        if cost <visit[zx][zy]:
                            visit[zx][zy]= cost
                            heapq.heappush(q, (cost,zx,zy))





while 1:

    INF = int(1e9)

    n=int(input().rstrip())
    if(n==0):
        break
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = []
    visit=[[10**5 for _ in range(n)] for _ in range(n) ]

    # 최단 거리 테이블을 모두 무한으로 초기화
    for i in range(n):
        e=list(map(int,input().split()))
        graph.append(e)

    dd()
    count+=1