import sys
input = sys.stdin.readline
d,n,m=map(int,input().split())
total=[]
for _ in range(n):
    total.append(int(input().rstrip()))
total.append(d)
total.sort()

left=0
right=d+1
now=0

def check(mid):
    now=0
    cnt=0
    for l in range(n+1):
        if total[l]-now<mid:
            if l!=n:
                cnt+=1
        else:
            now=total[l]
    return cnt


while left+1<right:
    mid=(left+right)//2
    t=check(mid)
    if t>m:
        right=mid
    else:
        left=mid

print(left)
