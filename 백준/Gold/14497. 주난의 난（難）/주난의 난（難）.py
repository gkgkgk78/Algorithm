import sys, copy, heapq
import heapq, math
from queue import PriorityQueue
from itertools import permutations, combinations, product
from collections import deque
from itertools import product

#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline


n,m=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
x1=x1-1
x2=x2-1
y1=y1-1
y2=y2-1


graph=[]
for _ in range(n):
    graph.append(list(map(str,input().rstrip())))


visit=[[0 for _ in range(m)] for _  in range(n)]
visit[x1][y1]=1

q=deque()
q.append((x1,y1,1))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

if(x1==x2 and y1==y2):
    print(0)
else:
    count = 1
    while 1:
        temp=[]
        while len(q)>0:
            a1,a2,a3=q.popleft()
            for i in range(4):
                zx=a1+dx[i]
                zy=a2+dy[i]
                if 0<=zx<n and 0<=zy<m:
                    if zx==x2 and zy==y2:
                        print(a3)
                        exit(0)
                    if(visit[zx][zy]==0):
                        visit[zx][zy]=1
                        if(graph[zx][zy]=='1'):
                            temp.append((zx,zy))
                            graph[zx][zy]='0'
                        elif (graph[zx][zy]=='0'):
                            q.append((zx, zy,count))
        for s1,s2 in temp:
            q.append((s1,s2,count+1))
        count=count+1