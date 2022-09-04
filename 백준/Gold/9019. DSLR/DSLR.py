import sys, copy
import heapq
from itertools import combinations
from collections import deque
input = sys.stdin.readline
import math

def bfs(e):
    q=deque()
    q.append((e,"t",0))#숫자 문자 횟수
    visit=set()
    visit.add(e)
    while q:
        a1,a2,a3=q.popleft()
        if a1==b:
            a2=a2[1:]
            print(a2)
            break
        else:
            t1=a1
            for i in range(4):
                t1 = a1
                # D
                if i==0:
                    if t1*2>9999:
                        t1=(t1*2)%10000
                    else:
                        t1=t1*2
                    e2=a2+"D"
                    if t1 not in visit:
                        visit.add(t1)
                        q.append((t1,e2,a3+1))
                #S
                elif i==1:
                    if t1==0:
                        t1=9999
                    else:
                        t1=t1-1
                    e2=a2+"S"
                    if t1 not in visit:
                        visit.add(t1)
                        q.append((t1,e2,a3+1))
                elif i==2:
                    aa=t1//1000
                    bb=t1%1000
                    t1=bb*10+aa
                    e2 = a2 + "L"
                    if t1 not in visit:
                        visit.add(t1)
                        q.append((t1,e2,a3+1))
                elif i==3:
                    aa=t1//10
                    bb=t1%10
                    t1=bb*1000+aa
                    e2 = a2 + "R"
                    if t1 not in visit:
                        visit.add(t1)
                        q.append((t1,e2,a3+1))

n=int(input().rstrip())
for i in range(n):
    a,b=map(int,input().split())
    bfs(a)

