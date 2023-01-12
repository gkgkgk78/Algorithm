import sys
input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
k=int(input().rstrip())

total=[0]*(n+1)
for i in range(2,n+1):
    if e[i-1]<e[i-2]:
        total[i]=total[i-1]+1
    else:
        total[i]+=total[i-1]

for l in range(k):
    a1,a2=map(int,input().split())
    print(total[a2]-total[a1])