import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

sumsu=[0]*3

def mama(a,b,n):
    if n==1:
        if graph[a][b]==-1:
            sumsu[0]+=1
        elif graph[a][b] == 0:
            sumsu[1] += 1
        else:
            sumsu[2] += 1
    else:
        start=graph[a][b]
        hk=0
        for i in range(a,n+a):
            for j in range(b,n+b):
                if start!=graph[i][j]:
                    mama(a,b,n//3)
                    mama(a,b+n//3,n//3)
                    mama(a,b+(n//3)*2,n//3)
                    mama(a+n//3,b,n//3)
                    mama(a+n//3,b+n//3,n//3)
                    mama(a+n//3,b+(n//3)*2,n//3)
                    mama(a+(n//3)*2,b,n//3)
                    mama(a+(n//3)*2,b+n//3,n//3)
                    mama(a+(n//3)*2,b+(n//3)*2,n//3)
                    hk=1
                    break
            if hk==1:
                break
        if hk==0:
            if graph[a][b] == -1:
                sumsu[0] += 1
            elif graph[a][b] == 0:
                sumsu[1] += 1
            else:
                sumsu[2] += 1

n=int(input().rstrip())
graph=[]
y=0
last=0
for i in range(n):
    tt=list(map(int,input().split()))
    hi=tt[0]
    if y==0:
        y=0
        for k in range(len(tt)):
            if hi!=tt[k]:
                y=1
                break
        if hi!=last:
            y=1
    graph.append(tt)
    last=tt[0]
if y==1:
    mama(0,0,n)
    for i in range(3):
        print(sumsu[i])
else:
    if graph[0][0] == -1:
        sumsu[0] += 1
    elif graph[0][0] == 0:
        sumsu[1] += 1
    else:
        sumsu[2] += 1
    for i in range(3):
        print(sumsu[i])