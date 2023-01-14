import sys
input = sys.stdin.readline

n,m=map(int,input().split())
e=list(map(int,input().split()))
e.sort()
sub=[0]*(n)
sub[0]=e[0]
for i in range(1,n):
    sub[i]+=e[i]+sub[i-1]

for _ in range(m):
    a1,a2=map(int,input().split())
    if a1==1:
        print(sub[a2-1])
    else:
        print(sub[a2-1]-sub[a1-2])