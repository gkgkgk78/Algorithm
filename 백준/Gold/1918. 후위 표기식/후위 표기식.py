import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


tt=input().rstrip()
ans=[]
d=deque()
for i in range(len(tt)):
    if tt[i].isalpha():
        ans.append(tt[i])

    else:
        if tt[i]=="(":
            d.append(tt[i])
        elif tt[i]=="*" or tt[i]=="/":
            while len(d)>0 and (d[-1]=="*"or d[-1]=="/") :
                ans+=d.pop()
            d.append(tt[i])
        elif tt[i]==")":
            while d and d[-1]!="(" :
                ans+=d.pop()
            d.pop()
        elif tt[i] == "+" or tt[i] == "-":
            while d and d[-1]!="(" :
                ans+=d.pop()
            d.append(tt[i])
while d:
    ans += d.pop()
for i in range(len(ans)):
    print(ans[i],end="")








