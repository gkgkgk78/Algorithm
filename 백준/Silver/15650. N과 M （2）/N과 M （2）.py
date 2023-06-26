import sys

input = sys.stdin.readline

n,m=map(int,input().split())


total=[]
isvisit=[0]*(n+1)

def dfs(now,cnt):

    if cnt>m:
        return
    if cnt==m:
        temp=[]
        for l in range(1,n+1):
            if isvisit[l]==1:
                temp.append(l)
        total.append(temp)
        return
    for k in range(now,n+1):
        if isvisit[k]==1:
            continue
        isvisit[k]=1
        dfs(k+1,cnt+1)
        isvisit[k]=0

dfs(1,0)

for k in total:
    print(*k)