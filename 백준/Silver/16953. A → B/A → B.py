import sys
from collections import deque
import math

input=sys.stdin.readline
sys.setrecursionlimit(10000)




def dfs(t1,t2):
    q=deque()
    q.append((t1,1))

    cnt=1
    while q:
        h,cnt=q.popleft()
        if h==t2:
            print(cnt)
            exit()
        g1=h*10+1
        g2=h*2

        for i in g1,g2:
            if 1<=i<=t2 :
                q.append((i,cnt+1))



a,b=map(int,input().split())




dfs(a,b)
print(-1)