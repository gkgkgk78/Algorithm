import sys

input = sys.stdin.readline

n,k=map(int,input().split())


a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1+=a2
a1.sort()
print(*a1)