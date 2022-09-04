import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque
sys.setrecursionlimit(10**9)

# input = sys.stdin.readline
input=sys.stdin.readline

n,m=map(int,input().split())

#0:북쪽 1:동쪽 2:남쪽 3:서쪽
position=[]

graph=[]
v1,v2,v3=map(int,input().split())
position.append(v1)
position.append(v2)
position.append(v3)


for i in range(n):
    e=list(map(int,input().split()))
    graph.append(e)
#dx=[-1,0,1,0]#상하좌우
#dy=[0,-1,0,1]
graph[v1][v2]=7
count=0
ex=0
while 1:
    if ex==1:
        break
    er=0
    if position==[9,2,3]:
        erer=0
    if position[2] == 0:  # 북쪽 방향 증가
        if graph[position[0]][position[1]-1]==0:
            er=1
    elif position[2] == 1:  # 동
        if graph[position[0]-1][position[1]]==0:
            er=1
    elif position[2] == 2:  # 남
        if graph[position[0]][position[1]+1]==0:
            er=1
    elif position[2] == 3:  # 서
        if graph[position[0]+1][position[1]]==0:
            er=1
    if er==1:
        graph[position[0]][position[1]] = 7
        count=0
        er=0
        if  position[2]==0:
            position[2]=3
        else:
            position[2]-=1  # 왼쪽방향으로 회전을함
        if position[2]==0:#북쪽 방향 증가
            position[0]=position[0]-1
            graph[position[0]][position[1]]=7
        elif position[2]==1:#동
            position[1] = position[1]+1
            graph[position[0]][position[1]] = 7
        elif position[2]==2:#남
            position[0] = position[0] + 1
            graph[position[0]][position[1]] = 7
        elif position[2]==3:#서
            position[1] = position[1] - 1
            graph[position[0]][position[1]] = 7
    else:
        while 1:
            if  position[2]==0:
                position[2]=3
            else:
                position[2]-=1  # 왼쪽방향으로 회전을함
            count+=1
            if position[2] == 0:  # 북쪽 방향 증가
                if graph[position[0]][position[1] - 1] == 0:
                    count=0

                    break
            elif position[2] == 1:  # 동
                if graph[position[0] - 1][position[1]] == 0:
                    count = 0
                    break
            elif position[2] == 2:  # 남
                if graph[position[0]][position[1] + 1] == 0:
                    count = 0
                    break
            elif position[2] == 3:  # 서
                if graph[position[0] + 1][position[1]] == 0:
                    count = 0
                    break

            if count>=4:
                if position[2] == 0:  # 북쪽 방향 증가
                    if graph[position[0]+1][position[1]]==1:
                        ex = 1
                        count = 0
                        break
                    else:
                        position[0]+=1
                        count = 0
                        break
                elif position[2] == 1:  # 동
                    if graph[position[0]][position[1]-1]==1:
                        ex = 1
                        count = 0
                        break
                    else:
                        position[1]-=1
                        count = 0
                        break

                elif position[2] == 2:  # 남
                    if graph[position[0]-1][position[1]]==1:
                        ex = 1
                        count = 0
                        break
                    else:
                        position[0]-=1
                        count = 0
                        break

                elif position[2] == 3:  # 서
                    if graph[position[0]][position[1]+1]==1:
                        ex = 1
                        count = 0
                        break
                    else:
                        position[1]+=1
                        count = 0
                        break


count=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==7:
            count+=1
print(count)



