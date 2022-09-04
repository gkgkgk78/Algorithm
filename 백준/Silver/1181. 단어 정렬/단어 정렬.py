import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
g=[]
t=1
py=[]
for i in range(n):
   t=(input().rstrip())
   if t not in py:
       tt=int(len(t))
       g.append([t,tt])
       py.append(t)

g=sorted(g,key=lambda x:(x[1],x[0]))

for i in range(len(g)):
    print(g[i][0])

