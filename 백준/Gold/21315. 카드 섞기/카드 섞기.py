import sys

from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))


def game(k,now):
    temp=deque()
    start=2**k
    last=deque()
    for i in range(start):
        ee=now.pop()
        temp.appendleft(ee)
    while now:
        last.append(now.popleft())
    for i in range(2,k+2):
        #직전에 올린 카드중에서 ~개의 카드를 더미의 맨위로 올린다
        nex=2**(k-i+1)
        ee=deque()
        for _ in range(nex):
            ee.appendleft(temp.pop())
        while temp:
            last.appendleft(temp.pop())
        temp=ee
    while temp:
        last.appendleft(temp.pop())
    return last
t=0
for i in range(1,n+1):
    if i==2:
        i=2
    for j in range(1,n+1):
        if 2**i>=n or 2**j>=n:
            t=1
            continue
        q=deque()
        for k in range(1,n+1):
            q.append(k)
        a1=game(i,q)
        a2=game(j,a1)
        if list(a2)==e:
            print(i,j)
            sys.exit(0)