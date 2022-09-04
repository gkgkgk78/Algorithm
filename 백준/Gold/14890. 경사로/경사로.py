import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque

# input = sys.stdin.readline
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(n):
    e=list(map(int,input().split()))
    graph.append(e)
count=0
for i in range(n):
    insert=[]
    hoho = 0
    if i==4:
        efef=334
    for j in range(n-1):
        if graph[i][j]<graph[i][j+1]:
            if graph[i][j+1]-graph[i][j]>1:#다음꺼가 나보다 클때
                hoho = 1
                break
            else:
                ct=0
                ee=[]
                if j-m+1<0:
                    ct=0
                else:
                    for t in range(j-m+1,j+1):
                        if (i,t) not in insert and graph[i][j]==graph[i][t]:
                            ct+=1
                            ee.append((i,t))
                if ct==m:
                    for kk in ee:
                        l1,l2=kk
                        insert.append((l1,l2))
                else:
                    hoho = 1
                    break
        elif graph[i][j]>graph[i][j+1]:#다음꺼가 나보다 작을때
            if graph[i][j]-graph[i][j+1]>1:#다음꺼가 나보다 클때
                hoho = 1
                break
            else:#진행이 가능하다면
                ct = 0
                ee = []
                if j+m+1>n:
                    ct=0
                else:
                    for t in range(j+1, j + m+1):

                        if (i, t) not in insert and graph[i][j+1] == graph[i][t]:
                            ct += 1
                            ee.append((i, t))
                if ct == m:
                    for kk in ee:
                        l1, l2 = kk
                        insert.append((l1, l2))
                    j=t
                else:
                    hoho = 1
                    break
    if hoho==0:
        count+=1

i=0
for i in range(n):
    insert=[]
    if i==4:
        efef=334
    hoho=0
    for j in range(n-1):

        if graph[j][i]<graph[j+1][i]:
            if graph[j+1][i]-graph[j][i]>1:#다음꺼가 나보다 클때
                hoho=1
                break
            else:
                ct=0
                ee=[]
                if j-m+1<0:
                    ct=0
                else:
                    for t in range(j-m+1,j+1):
                        if (t,i) not in insert and graph[j][i]==graph[t][i]:
                            ct+=1
                            ee.append((t,i))
                if ct==m:
                    for kk in ee:
                        l1,l2=kk
                        insert.append((l1,l2))
                else:
                    hoho = 1
                    break
        elif graph[j][i]>graph[j+1][i]:#다음꺼가 나보다 작을때
            if graph[j][i]-graph[j+1][i]>1:#다음꺼가 나보다 클때
                hoho = 1
                break
            else:#진행이 가능하다면
                ct = 0
                ee = []
                if j+m+1>n:
                    ct=0
                else:
                    for t in range(j+1, j + m+1):

                        if (t, i) not in insert and graph[j+1][i] == graph[t][i]:
                            ct += 1
                            ee.append((t,i))
                if ct == m:
                    for kk in ee:
                        l1, l2 = kk
                        insert.append((l1, l2))
                    j=t
                else:
                    hoho = 1
                    break
    if hoho==0:
        count+=1

print(count)

























