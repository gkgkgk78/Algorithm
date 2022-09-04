import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline



n=int(input().rstrip())

for i in range(n):
    count=0
    g=int(input().rstrip())
    ch=[]
    for j in range(g):
        s1,s2=map(int,input().split())
        ch.append([s1,s2])
    ch=sorted(ch,key=lambda a: a[0])
    max=ch[0][1]
    count=0
    for t in range(1,g):
        if max>ch[t][1]:
           count+=1
           max=ch[t][1]
    print(count+1)
