import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
e=[]
for _ in range(n):
    a1,a2=map(int,input().split())
    e.append([a1,a2])

e=sorted(e,key=lambda x:(x[1],x[0]))

for a1,a2 in e:
    print(a1,a2)