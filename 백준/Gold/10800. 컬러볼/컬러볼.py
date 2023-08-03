import sys
from collections import  deque
input = sys.stdin.readline

n=int(input().rstrip())
total=[]
color=[0]*(n+1)
beforez=0
before=deque()
sumz=0
ans=[0]*(n)
for i in range(n):
    a1,a2=map(int,input().split())
    #우선 같은 무게 가 있는거 제외
    total.append((a1,a2,i))
total=sorted(total,key=lambda x:(x[1],x[2]))

for a1,a2,ind in total:
    if beforez!=a2:
        while before:
            t1,t2=before.pop()
            color[t1]+=t2
            sumz+=t2
        beforez=a2
        before.append((a1,a2))
    else:
        before.append((a1, a2))
    ans[ind]=sumz-color[a1]

for i in ans:
    print(i)