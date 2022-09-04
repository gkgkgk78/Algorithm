import sys
from collections import deque
import math

input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(t1):


    for j in range(1,n+1):
        if visit[j]==0 and graph[t1][j]==1:
            visit[j]=1
            dfs(j)






n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)



while m>0:
    t1,t2=map(int,input().split())
    graph[t1][t2]=1
    graph[t2][t1]=1
    m=m-1


count=0
for i in range(1,n+1):
        if visit[i]==0:
            dfs(i)
            count=count+1

print(count)











