import sys, copy
import heapq,math
from itertools import combinations,permutations
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
import functools,operator


before_go='right'

mama=int(input().rstrip())
tmap=[[0]*(mama+1) for _ in range(mama+1)]

apple=[]
ap_size=int(input().rstrip())
for i in range(ap_size):
    x,y=map(int,input().split())
    tmap[x][y]=1
g=int(input().rstrip())
time=[]
ver=[]
for i in range(g):
    x, y = map(str, input().split())
    time.append((int(x),y))

start_x,start_y=1,1
count=0
dead_line=time[0][0]
origin_x,origin_y=1,1
tmap[1][1]=2
body=[]
body.append((1,1))
while 1:

    if before_go == 'right':
                start_y += 1
    elif before_go == 'left':
                start_y -= 1
    elif before_go == 'down':
                start_x += 1
    elif before_go == 'up':
                start_x -= 1
    if start_x<1 or start_x>mama or start_y<1 or start_y>mama:
        print(count+1)
        exit(0)
    elif tmap[start_x][start_y]==2:#자기 자신과 부딪힐 경우
        print(count+1)
        exit(0)
    else:#사과를 먹거나 아닐경우
        if tmap[start_x][start_y]==1:
            tmap[start_x][start_y] = 2
            body.append((start_x,start_y))
            count+=1
        else:#사과 안먹 었엉
            tmap[start_x][start_y] = 2
            if len(body)==0:
                body.append((start_x, start_y))
                count += 1
            else:
                for i in body:
                    g1,g2=i
                    tmap[g1][g2]=0
                    body.pop(0)
                    break

                body.append((start_x, start_y))
                count += 1
    if len(time)>0 and count ==time[0][0]:#방향 전환 해야 할때
        if before_go=='right':
            fef=2
            if time[0][1]=='D':#오른쪽 90도
                #start_x += 1
                before_go='down'
            else:
                #start_x -= 1
                before_go='up'
        elif before_go=='left':
            if time[0][1] == 'D':  # 오른쪽 90도
                #start_x -= 1
                before_go='up'
            else:
                #start_x += 1
                before_go='down'
        elif before_go=='down':
            if time[0][1] == 'D':  # 오른쪽 90도
                #start_y -= 1
                before_go='left'
            else:
                #start_y += 1
                before_go='right'
        elif before_go=='up':
            if time[0][1] == 'D':  # 오른쪽 90도
                #start_y += 1
                before_go='right'
            else:
                before_go='left'
                #start_y -= 1
        del time[0]






