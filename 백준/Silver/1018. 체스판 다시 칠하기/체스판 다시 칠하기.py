import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

wb=[ "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
     ]
bw=["BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"]
n,m=(map(int,input().split()))
graph=list((input().rstrip()) for _ in range(n))
mina=64000000



def wcnt(w,q):
    cnt=0
    for i in range(8):
        for j in range(8):
            if graph [w+i][q+j]!=wb[i][j]:
                cnt+=1
    return cnt
def bcnt(w,q):
    cnt=0
    for i in range(8):
        for j in range(8):
            if graph [w+i][q+j]!=bw[i][j]:
                cnt+=1
    return cnt







for i in range(0,n-7):

    for j in range(0,m-7):
        g1,g2=i,j
        cn=min(wcnt(i,j),bcnt(i,j))
        mina=min(mina,cn)
print(mina)


























