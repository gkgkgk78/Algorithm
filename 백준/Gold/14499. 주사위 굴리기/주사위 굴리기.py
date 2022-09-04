import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque

# input = sys.stdin.readline
input=sys.stdin.readline

from bisect import bisect_right, bisect_left
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n,m,x,y,k=map(int,input().split())
dice=[0,0,0,0,0,0]#위 뒤

graph=[]
for _ in range(n):
    e=list(map(int,input().split()))
    graph.append(e)
com=list(map(int,input().split()))
nx, ny = x, y
def turn(i):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if i==1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif i==2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] =c,b,f,a,e,d

    elif i == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] =b,f,c,d,a,e

    elif i == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] =e,a,c,d,f,b

for i in com:
    nx += dx[i - 1]
    ny += dy[i - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i - 1]
        ny -= dy[i - 1]
        continue
    turn(i)
    if graph[nx][ny]==0:
        graph[nx][ny]=dice[-1]
    else:
        dice[-1]=graph[nx][ny]
        graph[nx][ny]=0
    print(dice[0])