import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline


a=int(input())
leftheap = []
rightheap=[]
for i in range(0,a):
    b=(input().rstrip())

    b=int(b)
    if len (leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-b,b))
    else:
        heapq.heappush(rightheap, (b, b))
    if rightheap and leftheap[0][1]>rightheap[0][0]:
        g1,g2=heapq.heappop(leftheap)
        t1,t2=heapq.heappop(rightheap)
        heapq.heappush(leftheap, (-t1, t1))
        heapq.heappush(rightheap, (g2, g2))
    print(leftheap[0][1])