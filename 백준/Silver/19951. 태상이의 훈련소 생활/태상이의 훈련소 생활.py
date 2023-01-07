import sys
input = sys.stdin.readline

n,m=map(int,input().split())

sumz=[0]*(n+1)
arr=list(map(int,input().split()))

for l in range(m):
    a1,a2,a3=map(int,input().split())

    a1-=1
    a2-=1
    sumz[a1]+=a3
    sumz[a2+1]-=a3

for i in range(0,n):
    sumz[i+1]+=sumz[i]
for i in range(n):
    arr[i]+=sumz[i]

print(*arr)