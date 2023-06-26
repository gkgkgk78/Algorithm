import sys

input = sys.stdin.readline

n,m=map(int,input().split())

total = []
isvisit = [0] * (n )
isselected = [0] * (m)

e=list(map(int,input().split()))
e.sort()



def perm(start,cnt):
    if cnt==m:
        temp=[]
        for l in range(m):
            temp.append(e[isselected[l]])
        total.append(temp)
        return
    for l in range(n):
        if isvisit[l]==1:
            continue
        isvisit[l]=1
        isselected[cnt]=l
        perm(l+1,cnt+1)
        isvisit[l]=0

perm(0,0)
for k in total:
    print(*k)