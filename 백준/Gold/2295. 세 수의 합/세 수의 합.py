import sys
input = sys.stdin.readline
n=int(input().rstrip())
e=[]
for _ in range(n):
    e.append(int(input().rstrip()))

add=[]
for i in e:
    for j in e:
        add.append(i+j)
add.sort()

ans = -sys.maxsize
aa=len(add)

def bi(now):
    left=-1
    right=len(add)
    while left+1<right:
        mid=(left+right)//2
        if add[mid]>=now:
            right=mid
        else:
            left=mid
        if add[mid]==now:
            return 1
    if right==len(add):
        return 0
    if right<len(add):
        if add[right]==now:
            return 1
    return 0

for i in e:
    for j in e:
        ne=i-j
        if ne>0:
            left = bi(ne)
            if left==1:
                ans=max(ans,i)

print(ans)