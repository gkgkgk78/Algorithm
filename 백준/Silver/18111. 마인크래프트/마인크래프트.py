import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline


n,m,b=map(int,input().split())


graph=[]
mins=999999
result=0
maxs=-1
time=1000000000000000000000
hei=[0]*257

for i in range (n):
    h=list(map(int,input().split()))
    for j in range(m):
        hei[h[j]]+=1

    graph.append(h)


mins=min(map(min,graph))
maxs=max(map(max,graph))

for kk in range(mins,maxs+1):
    plus=0
    minus=0

    for i in range(0,len(hei)):
            h=i-kk
            # if hei[i]!=0:
            #     print(i,kk*hei[i],i*hei[i])
            if h>0:
                minus+=h*hei[i]
            elif h<0:
                plus-=h*hei[i]

    if minus+b>=plus:
        timez=minus*2+plus
        if timez<=time:

            time=timez
            result=kk

print(time,result)