import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math
t=input().rstrip()
g=input().rstrip()
hi=g[-1]
d=[]
for i in range(len(t)):
    if t[i]!=hi:
        d.append(t[i])
    else:
        fy=0
        d.append(t[i])
        go = len(d)-1
        if len(d)>0:
            for j in range(len(g)-1,-1,-1):
                if g[j]==d[go]:
                    go-=1
                elif g[j]!=d[go]:
                    fy=1
                    break
            if fy==0:
                for k in range(len(g)):
                    d.pop()
if d:
    for i in d:
        print(i,end="")
else:
    print("FRULA")