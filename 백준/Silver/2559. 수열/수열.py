import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque
sys.setrecursionlimit(10**9)

# input = sys.stdin.readline
input=sys.stdin.readline

n,m=map(int,input().split())
e=list(map(int,input().split()))

sumz=0
for i in range(m):
    sumz+=e[i]
co_max=[]
io=1
co_max.append(sumz)
for i in range(0,len(e)-m):
    io+=1
    sumz=sumz-e[i]+e[i+m]
    co_max.append(sumz)

print(max(co_max))
































