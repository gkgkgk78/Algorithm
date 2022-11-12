import sys, copy, heapq
import heapq, math
from queue import PriorityQueue

input = sys.stdin.readline
n,m=map(int,input().split()) 

#우선은 각 마을에 오는 보내는 마을을 구한후에,
mo=[0 for _ in range(n+1)]
t=int(input().rstrip())

total=[]
for _ in range(t):
    a1,a2,a3=map(int,input().split())
    total.append((a1,a2,a3))


total=sorted(total,key=lambda x:(x[1],x[0]))

answer=0
for i in range(t):

    a1,a2,a3=total[i]
    temp=0
    for l in range(a1,a2):
        temp=max(temp,mo[l])
    now_max=temp
    #있는 값중에 최대값을 찾은 후에
    can=0
    if(a3+now_max<=m):
        can=a3
    else:
        can=m-now_max

    if(can>0):
        answer+=can
        for l in range(a1,a2):
            mo[l]+=can


print(answer)