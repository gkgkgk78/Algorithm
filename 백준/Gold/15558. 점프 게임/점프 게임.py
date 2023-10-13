import sys
import math
from collections import deque
import heapq
input = sys.stdin.readline

n,k=map(int,input().split())
graph=[]

left=[0]+list(map(int,input().rstrip()))
right=[0]+list(map(int,input().rstrip()))
graph.append(left)
graph.append(right)
visit=[[0]*(n+2)for _ in range(2)]


def ch(i):
    if i==0:
        return 1
    else:
        return 0


def bfs():
    q=deque()

    time = 1
    q.append((1,0))#현재 인덱스 왼쪽을 의미함
    while 1:
        temp=deque()
        if len(q)==0:
            break
        while q:
            now,where=q.popleft()#현재 인덱스, 방향
            if graph[where][now]==0:
                continue
            #한칸앞
            if now+1>n:
                print(1)
                sys.exit()
            else:
                if visit[where][now+1]==0 and graph[where][now+1]==1:
                    visit[where][now+1]=1
                    temp.append((now+1,where))
            #한칸뒤
            if visit[where][now-1]==0 and graph[where][now-1]==1:
                    visit[where][now-1]=1
                    temp.append((now-1,where))
            #반대편줄
            wh=ch(where)
            if now+k>n:
                print(1)
                sys.exit()
            else:
                if visit[wh][now+k] == 0 and graph[wh][now+k] == 1:
                    visit[wh][now+k] = 1
                    temp.append((now+k, wh))
        q=temp

        graph[0][time]=0
        graph[1][time] = 0
        time+=1

bfs()
print(0)