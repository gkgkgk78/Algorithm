import sys

input = sys.stdin.readline

n, m = map(int, input().split())
e = list(map(int, input().split()))

left = -1
right = max(e) + 1

def count(mid):
    check=0
    for i in e:
        temp=i-mid
        if temp>0:
            check+=temp
    if check>=m:
        return 1
    else:
        return 0

while left+1<right:
    mid=(left+right)//2
    temp=count(mid)
    if temp==1:
        left=mid
    else:
        right=mid
print(left)