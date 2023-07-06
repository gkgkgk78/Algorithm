import sys
from collections import deque
input=sys.stdin.readline

k,l=map(int,input().split())
e=[]
total=dict()
for _ in range(l):
    a=str(input().rstrip())
    if a not in total:
        total[a]=1
    else:
        total[a]+=1
    e.append(a)
e=deque(e)
temp=deque()
while e:
    a1=e.popleft()
    if total[a1]==1:
        temp.append(a1)
    else:
        total[a1]-=1

for i in range(k):
    if temp:
        print(temp.popleft())