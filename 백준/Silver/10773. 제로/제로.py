import sys
from collections import deque
input = sys.stdin.readline

k=int(input().rstrip())
q=deque()
for _ in range(k):
    a=(int(input().rstrip()))
    if a==0:
        q.pop()
    else:
        q.append(a)

print(sum(q))