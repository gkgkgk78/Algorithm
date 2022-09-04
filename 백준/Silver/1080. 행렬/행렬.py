import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline



n,m=map(int,input().split())
ori=[list(map(int,input().rstrip())) for i in range (n)]
fin=[list(map(int,input().rstrip())) for i in range (n)]


if n<3 and m<3:
    if ori != fin :
        print(-1)
    else:
        print(0)
    exit(0)

cnt=0
for i in range (n-2):
    for j in range (m-2):
        if i<n-2 and j<m-2:
            if ori[i][j]!=fin[i][j]:
                for t1 in range(i,i+3):
                    for t2 in range(j,j+3):
                        if ori[t1][t2]==0:
                            ori[t1][t2]=1
                        else:
                            ori[t1][t2] = 0
                cnt+=1

if ori != fin:
    print(-1)
else:
    print(cnt)