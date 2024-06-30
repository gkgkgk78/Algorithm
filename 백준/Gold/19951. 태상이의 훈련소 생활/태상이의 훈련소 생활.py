import sys
input = sys.stdin.readline

n,m=map(int,input().split())
e=list(map(int,input().split()))
data=[0]*(n+1)
for _ in range(m):
    a1,a2,a3=map(int,input().split())
    a1-=1
    a2-=1
    data[a1]+=a3
    data[a2+1]-=a3
for i in range(1,n+1):
    data[i]+=data[i-1]
for i in range(n):
    e[i]+=data[i]
print(*e)