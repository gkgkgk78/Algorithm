import sys
input = sys.stdin.readline
from collections import deque
n=int(input().rstrip())

total=[]
for _ in range(n):
    e=int(input().rstrip())
    total.append(e)

total=sorted(total,key=lambda x:-x)
total=deque(total)
now=-sys.maxsize

for l in range(len(total)):
    a1=total.popleft()
    temp=a1*(l+1)
    now=max(now,temp)
print(now)