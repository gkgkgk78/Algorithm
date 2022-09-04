import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

#한 물통이 비거나 , 다른 한 물통이 가득 찰 때까지 물을 붓는다



n=int(input())
count=0
while n>0:
    check=[]
    h=input().rstrip('\n')
    ho=0
    for i in range(0,len(h)):
        if h[i] not in check:
            check.append(h[i])
        elif h[i] in check:
            if check[-1]!=h[i]:
                ho=1
                break
    if ho==0:
        count=count+1
    n=n-1
print(count)