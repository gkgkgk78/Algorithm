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

n,m=map(int,input().split())

#최소 힙의 형태로 정렬이 된다
heap=[]

julury=[]
bag=[]

for _ in range(n):
    a1,a2=map(int,input().split())
    julury.append((a1,a2))
for _ in range(m):
    bag.append(int(input().rstrip()))

julury.sort()

bag.sort()
sumz=[]

temp=[]
result=0
for l in bag:
    while julury and l>=julury[0][0]:
        heapq.heappush(temp,-julury[0][1])
        heapq.heappop(julury)
    if temp:
        result+=heapq.heappop(temp)

print(-result)