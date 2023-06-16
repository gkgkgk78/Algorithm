import sys

input = sys.stdin.readline
n,m = map(int,input().split())
e=list(map(int,input().split()))

sumz=[0]*(n+1)

for _ in range(m):
    a,b,k=map(int,input().split())
    sumz[a-1]+=k
    sumz[b]-=k

for i in range(1,n):
    sumz[i]+=sumz[i-1]

for i in range(n):
    e[i]+=sumz[i]
print(*e)