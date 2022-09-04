import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque

input=sys.stdin.readline

from bisect import bisect_right, bisect_left

n=int(input().rstrip())
graph=[list(map(int,input().split())) for _ in range(n)]
t=[]
g=n//2
for i in range(n):
    t.append(i)
go=list(combinations(t,g))

ea=99999
for le in go:
    one=list(le)
    two=[]
    for i in t:
        if i not in one:
            two.append(i)


    one_sum=0
    two_sum=0
    ae=one
    ee=list(permutations(ae,2))
    for l in ee:
        a1,a2=l
        one_sum+=graph[a1][a2]
    ah = two
    eh = list(permutations(ah, 2))
    for l in eh:
        a1, a2 = l
        two_sum += graph[a1][a2]
    ea=min(abs(two_sum-one_sum),ea)
print(ea)



