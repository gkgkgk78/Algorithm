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

te=[]
for _ in range(n):
    a1,a2=map(int,input().split())
    te.append((a1,a2))
te.sort()

ui=[]
heapq.heappush(ui,te[0][1])
count=1
for p in range(1,n):
    heapq.heappush(ui,te[p][1])
    if ui[0]>te[p][0]:
        count+=1
    else:
        heapq.heappop(ui)

print(count)