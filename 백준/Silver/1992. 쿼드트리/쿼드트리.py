import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline


n=int(input().rstrip())
graph=[list(map(int,input().rstrip())) for _ in range(n)]

result=[]

def st(x,y,n):

    go=graph[x][y]
    for i in range(x,x+n):
        for j in range(y, y + n):
            if graph[i][j]!=go:
                result.append("(")
                st(x,y,n//2)
                st(x,y+n//2,n//2)
                st(x+n//2 ,y,n//2)
                st(x+n//2,y+n//2,n//2 )
                result.append(")")
                return
    if go==0:
      result.append("0")
    elif go==1:
        result.append("1")


st(0,0,n)
for i in result:
    print(i,end="")












