import sys

from collections import deque
import heapq

input = sys.stdin.readline

r,c=map(int,input().split())

total=[""]*(c)
count=0
for _ in range(r):
    e=list(map(str,input().rstrip()))
    for i in range(c):
        total[i]+=e[i]
answer=[[]for _ in range(c-1)]
test=0
for i in range(1,r):
    now=dict()
    last=0
    for j in range(c):

        temp=total[j][i:r]
        if temp in now:
            last=1
            break
        else:
            now[temp]=1
    if last==1:
        break
    test+=1
    if test==c-1:
        break
print(test)