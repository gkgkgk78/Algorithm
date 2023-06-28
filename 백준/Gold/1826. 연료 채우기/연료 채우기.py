import sys
import heapq
from collections import deque
input = sys.stdin.readline
n=int(input().rstrip())
q=[]
for _ in range(n):
    vertex,fuel=map(int,input().split())
    q.append((vertex,fuel))

q=sorted(q,key=lambda x:(x[0]))
goal,now_fuel=map(int,input().split())

q=deque(q)
qq=[]
count=0
while 1:

    if now_fuel >= goal:
        print(count)
        break

    #내가 갈수 있는 곳중에 최대 연료를 주는 것을 선택 하도록 하자.
    while q:
        vertex,fuel=q.popleft()
        if vertex<=now_fuel:
            heapq.heappush(qq,(-fuel,vertex))
        else:
            q.appendleft((vertex,fuel))
            break

    if len(qq)==0 and now_fuel<goal:
        print(-1)
        break

    nfuel,vertex=heapq.heappop(qq)
    now_fuel+=(-nfuel)
    count+=1