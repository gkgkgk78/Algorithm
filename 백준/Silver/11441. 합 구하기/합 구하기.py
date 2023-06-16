import sys
input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))

sub=[0]*(n+1)
sub[0]=e[0]
for i in range(1,n):
    sub[i]+=sub[i-1]+e[i]

k=int(input().rstrip())

for _ in  range(k):
    a1,a2=map(int,input().split())

    if a1==1:
        print(sub[a2-1])
    else:
        print(sub[a2-1]-sub[a1-2])