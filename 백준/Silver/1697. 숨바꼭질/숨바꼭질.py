import sys
from collections import deque
import math

input=sys.stdin.readline

# def dfs(t):
#     visit_list[t]=1
#     print(t,end=" ")
#     for i in range(1,n+1):
#         if graph[t][i]==1 and visit_list[i]==0:
#             dfs(i)


def bfs(t1,t2):
    q=deque()

    q.append(t1)


    while q:

        g1=q.popleft()
        dx = [g1 - 1, g1 + 1, g1 * 2]
        if g1==t2:
            print(count[g1])
            break
        else:

            for i in range (0,3):
                 hh=dx[i]
                 if  0<=hh<=MAX and count[hh]==0  :
                    q.append(hh)
                    count[hh]=count[g1]+1



MAX = 10 ** 5
n,m = map(int,input().split())


count = [0] * (MAX + 1)


bfs(n,m)







