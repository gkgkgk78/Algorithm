import sys

input = sys.stdin.readline

n,m=map(int, input().split())
e=list(map(int,input().split()))

left=0
right=m-1
now=sum(e[:right+1])
ma=sum(e[:right+1])


while right+1<n:
    right+=1
    now+=e[right]
    now-=e[left]
    left+=1
    ma=max(ma,now)

print(ma)