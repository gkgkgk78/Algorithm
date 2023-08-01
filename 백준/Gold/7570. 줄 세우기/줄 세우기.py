import sys

input = sys.stdin.readline

n = int(input().rstrip())

position=[-1]*(n+1)
e = [0]+list(map(int,input().split()))
for i in range(1,n+1):
    position[e[i]]=i

cnt=1
ans=-1
for i in range(1,n):
    if position[i]<position[i+1]:
        cnt+=1
        ans=max(ans,cnt)
    else:
        cnt=1
if ans==-1:
    print(0)
else:
    print(n-ans)