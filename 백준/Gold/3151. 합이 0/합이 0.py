import sys

input = sys.stdin.readline

n = int(input().rstrip())
e = list(map(int, input().split()))
e.sort()
total=dict()
for i in e:
    if i not in total:
        total[i]=1
ans = 0
def lower(arr,now,left,right):

    left=left
    right=right
    while left+1<right:
        mid=(left+right)//2
        if arr[mid]>=now:
            right=mid
        else:
            left=mid
    return right

def upper(arr, now, left, right):
    left=left
    right=right
    while left+1<right:
        mid=(left+right)//2
        if arr[mid]<=now:
            left=mid
        else:
            right=mid
    return left+1

for i in range(n):
    now = e[i]
    for j in range(i+1,n):
        ne=-(e[i]+e[j])
        if ne in total:
            a1=lower(e,ne,j,n)
            a2=upper(e,ne,j,n)
            ans+=(a2-a1)

print(ans)