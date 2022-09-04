import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline


n=int(input().rstrip())
graph=[list(map(int,input().split())) for _ in range(n)]

white=0
blue=0

def st(x,y,n):
    global white,blue
    go=graph[x][y]
    for i in range(x,x+n):
        for j in range(y, y + n):
            if graph[i][j]!=go:
                st(x,y,n//2)
                st(x,y+n//2,n//2)
                st(x+n//2 ,y,n//2)
                st(x+n//2,y+n//2,n//2 )
                return
    if go==0:
      white+=1
    elif go==1:
        blue+=1


st(0,0,n)
print(white)
print(blue)
