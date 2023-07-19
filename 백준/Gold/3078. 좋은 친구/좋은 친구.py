import sys
from collections import deque
input = sys.stdin.readline

n,k=map(int,input().split())
total=[]
for _ in range(n):
    total.append(len(input().rstrip()))
fi=[deque()for _ in range(21)]
ans=0
index=0
for i in total:
    while fi[i] and index-fi[i][0]>k:
        fi[i].popleft()
    ans+=len(fi[i])
    fi[i].append(index)
    index+=1
print(ans)