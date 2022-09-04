import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque

# input = sys.stdin.readline
input=sys.stdin.readline

#0은 빈칸 6은 벽 1~5는 cctv를 나타냄
n,m=map(int,input().split())
#cctv 1,2,3,4,5가 존재함
cctv=[]
graph=[]
for i in range((n)):
    g=list(map(int,input().split()))
    for j in range(0,len(g)):
        if g[j]>=1 and g[j]<=5:
            cctv.append((g[j],i,j))#어떤 cctv인지 그리고 인덱스
    graph.append(g)
#1:u d l r
#2:lr ud
#3:ur rd dl lu
#4:lur urd rdl dlu
#5:uldr
cctv_all=[]

for i in cctv:
    app=[]
    if i[0]==1:
        app.append(['u',i[1],i[2]])
        app.append(['d',i[1],i[2]])
        app.append(['l',i[1],i[2]])
        app.append(['r',i[1],i[2]])

    elif i[0]==2:
        app.append(['lr',i[1],i[2]])
        app.append(['ud',i[1],i[2]])
    elif i[0] == 3:
        app.append(['ur',i[1],i[2]])
        app.append(['rd',i[1],i[2]])
        app.append(['dl',i[1],i[2]])
        app.append(['lu',i[1],i[2]])
    elif i[0] == 4:
        app.append(['lur',i[1],i[2]])
        app.append(['urd',i[1],i[2]])
        app.append(['rdl',i[1],i[2]])
        app.append(['dlu',i[1],i[2]])
    elif i[0] == 5:
        app.append(['uldr',i[1],i[2]])

    cctv_all.append(app)
cctv_all=list(product(*cctv_all))
#여기까지 해서 모든 방향과 조합을 구한거임 그후에
#print(graph)
op=10**9
for i in cctv_all:
    #새로 만들게 할 것은 7로 하자구
    for j in i:
        #print(j[1],j[2])
        t=j[0]
        for k in t:
            if k =='l':
                tx,ty=j[1],j[2]
                while ty-1>=0:
                    if graph[tx][ty-1]>=0 and graph[tx][ty-1]<=5 or graph[tx][ty-1]==7:
                        if graph[tx][ty-1]==0:
                            graph[tx][ty-1]=7
                        ty=ty-1
                    else:
                        break
            elif k  == 'r':
                tx, ty = j[1], j[2]
                while ty+1<m:
                    if graph[tx][ty+1] >=0 and graph[tx][ty+1]<=5 or graph[tx][ty+1]==7:
                        if graph[tx][ty+1]==0:
                            graph[tx][ty+1] = 7
                        ty = ty + 1
                    else:
                        break
            elif k  == 'u':
                tx, ty = j[1], j[2]
                while tx-1 >= 0:
                    if graph[tx-1][ty] >=0 and graph[tx-1][ty]<=5 or graph[tx-1][ty]==7:
                        if graph[tx-1][ty]==0:
                            graph[tx-1][ty] = 7
                        tx=tx-1
                    else:
                        break
            elif k  == 'd':
                tx, ty = j[1], j[2]
                while tx+1 <n:
                    if graph[tx+1][ty] >= 0 and graph[tx+1][ty]<=5 or graph[tx+1][ty]==7:
                        if graph[tx+1][ty]==0:
                            graph[tx+1][ty] = 7
                        tx = tx + 1
                    else:
                        break
    sum=0
    for t1 in range(n):
        for t2 in range(m):
            if  graph[t1][t2]==0:
                sum+=1
            elif graph[t1][t2]==7:
                graph[t1][t2]=0
    op=min(sum,op)
print(op)


