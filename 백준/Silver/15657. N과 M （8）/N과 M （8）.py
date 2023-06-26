import sys

input = sys.stdin.readline

n,m=map(int,input().split())
e=list(map(int,input().split()))
e.sort()
total = []
isvisit = [0] * (n )
isselected = [0] * (m)

def comb(start,cnt):
    temp=[]
    if cnt==m:
        for l in isselected:
            temp.append(e[l])
        total.append(temp)
        return
    for k in range(start,n):
        isselected[cnt]=k
        comb(k,cnt+1)
comb(0,0)
for k in total:
    print(*k)