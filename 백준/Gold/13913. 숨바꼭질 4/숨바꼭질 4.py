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
    road = [[] for i in range(MAX+1)]
    count = [0] * (MAX + 1)
    while q:

        g1=q.popleft()
        dx = [g1 - 1, g1 + 1, g1 * 2]
        if g1==t2:
            print(count[g1])
            #coco=[z]
            arr=[]
            tt=t2
            for i in range(0,count[g1]):

                hi="".join(map(str,road[tt]))
                hi=int(hi)
                
                arr.append(hi)
                g3="".join(map(str,road[tt]))
                tt=int(g3)


            arr.reverse()
            arr.append(g1)
            print(*arr)
            break
        else:

            for i in range (0,3):
                 hh=dx[i]
                 if  0<=hh<=MAX and count[hh]==0  :
                    q.append(hh)
                    count[hh]=count[g1]+1

                    if len(road[g1])==0:
                        road[hh].append(g1)
                    else:
                        # for i in range (0,len(g)):
                        #     gt=g[i]
                        #     road[hh].append(gt)

                        road[hh].append(g1)


MAX = 10 ** 5
n,m = map(int,input().split())




bfs(n,m)







