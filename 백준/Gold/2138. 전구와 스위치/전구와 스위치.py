import sys
from  copy import deepcopy
input = sys.stdin.readline

n = int(input().rstrip())
first = list(map(int, input().rstrip()))
second = list(map(int, input().rstrip()))

#우선 안누르고 시작 하자

def go(f):
    co=0
    now=deepcopy(f)
    for i in range(1,n):
        if now[i-1]==second[i-1]:
            continue

        co+=1

        for j in range(i-1,i+2):
            if j>=n:
                break
            now[j]=1-now[j]

    if now==second:
        return co
    else:
        return -1

f1=go(first)
first[0]=1-first[0]
first[1]=1-first[1]
f2=go(first)

if f1==-1 and f2==-1:
    print(-1)
else:
    ans=sys.maxsize
    if f1!=-1:
        ans=min(ans,f1)
    if f2!=-1:
        ans=min(ans,f2+1)
    print(ans)