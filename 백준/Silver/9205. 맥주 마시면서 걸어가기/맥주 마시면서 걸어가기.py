import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque
from collections import Counter
#sys.setrecursionlimit(10**5)

#input = sys.stdin.readline
input=sys.stdin.readline

from bisect import bisect_right, bisect_left


#맥주 한 박스에는 맥주가 20개 들어있다.
#목이 마르면 안되기 때문에 50미터에 한병씩 마시려고 한다.

n=int(input().rstrip())

def bfs(x,y,lx,ly):
    q=deque()
    visit=[]
    q.append((x,y))
    visit.append((x,y))
    op=0
    while q:
        a1,a2=q.popleft()
        if abs(lx - a1) + abs(ly - a2) <= 1000:
            op = 1
            break
        if op==1:
            break
        for t in pu:
            b1,b2=t
            h1=abs(a1-b1)
            h2=abs(a2-b2)
            cal=(h1+h2)//50
            if cal<=20:
                if(b1,b2) not in visit:
                    visit.append((b1,b2))
                    q.append((b1,b2))
                    if abs(lx-b1)+abs(ly-b2)<=1000:
                        op=1
                        break
    if op==1:
        return 1
    else:
        return 0



for _ in range(n):
    h=int(input().rstrip())
    home_x,home_y=map(int,input().split())
    pu=[]
    if h!=0:
        for _ in range(h):
            a1,a2=map(int,input().split())
            pu.append((a1,a2))
    else:
        pu.append((0,0))
    last_x,last_y=map(int,input().split())
    u=bfs(home_x,home_y,last_x,last_y)
    if u==1:
        print("happy")
    else:
        print("sad")













