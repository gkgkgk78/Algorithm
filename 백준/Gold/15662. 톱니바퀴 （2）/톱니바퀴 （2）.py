import sys,copy
from itertools import combinations

from collections import deque

input=sys.stdin.readline



def rotate(t1,t2):
    for i in range(0,a):
        if (check[i]==1 and order!=t2) or i==t1:
            if order[i]==1:

                graph[i].appendleft(graph[i].pop())
            else:

                graph[i].append(graph[i].popleft())


a= int(input())

graph=[deque(map(int,input().rstrip())) for _ in range(a)]
order=[0]*a

k=int(input())

for i in range(k):
    t1,t2=map(int,input().split())
    t1=t1-1
    #2과 6이 회전 되는 상태에 놓임 a-1번 확인 하면 됨
    order[t1]=t2
    check=[0]*a
    check[t1]=1
    for j in range(t1,0,-1):
        if graph[j][6]==graph[j-1][2]:
            order[j-1]=order[j]
        else:
            if order[j]==-1:
                order[j-1]=1
            else:
                order[j-1]=-1
            check[j-1]=1
        if check[j]==0:
                check[j - 1] = 0
    for j in range(t1, a-1):
        if graph[j][2]==graph[j+1][6]:
            order[j+1]=order[j]
        else:
            if order[j]==-1:
                order[j+1]=1
            else:
                order[j+1]=-1
            check[j +1] = 1
        if check[j]==0:
                check[j + 1] = 0

    rotate(t1,t2)
    k -= 1


count=0
for i in range(0,a):
    if graph[i][0]==1:
       count=count+1

print(count)
















































