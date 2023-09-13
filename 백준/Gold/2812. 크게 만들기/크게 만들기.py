import sys
input = sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
e=list(map(int,input().rstrip()))
co=0

ind=1
ans=deque()
last=deque()
for i in e:
    last.append(i)
ans.append(e[0])
last.popleft()

while last:

    n1=last.popleft()
    t=0
    aa=ans.pop()
    if aa<n1:
        ans.append(aa)
        while 1:
            if len(ans)>0:
                ee = ans.pop()
                if ee<n1:
                    co+=1
                    if co==k:
                        t=1
                        ans.append(n1)
                        break

                else:
                    ans.append(ee)
                    ans.append(n1)
                    break
            else:
                ans.append(n1)
                break

    else:
        ans.append(aa)
        ans.append(n1)

    if t==1:
        while last:
            ans.append(last.popleft())
        break
for i in range(k-co):
    ans.pop()
an=""
while ans:
    an+=(str)(ans.popleft())
print(an)