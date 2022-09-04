import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline



n, m = map(int, input().split())

a = set()
t1=list(map(int,input().split()))
for i in range (n):
    a.add(t1[i])


b = set()
t2=list(map(int,input().split()))
for i in range(m):
    b.add(t2[i])
t3=a-b
t4=b-a


result = sorted(list(t3 | t4))
print(len(result))

