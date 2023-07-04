import sys

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
e.sort()
k=int(input().rstrip())
ss=list(map(int,input().split()))


def dd(end):
    left=0
    right=len(e)-1

    if e[right]==end:
        print(1)
        return 
    while left+1<right:
        mid=(left+right)//2

        if e[mid]<=end:
            left=mid
        else:
            right=mid
    if e[left]==end:
        print(1)
    else:
        print(0)

for l in ss:
    dd(l)