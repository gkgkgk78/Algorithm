import sys

input = sys.stdin.readline

n,m=map(int,input().split())

total=[]
last=dict()
for _ in range(n):
    e=list(map(int,input().split()))
    temp=sorted(e)
    now = ""
    for j in temp:
        now += str(e.index(j))
    if now not in last:
        last[now] = 0
    last[now] += 1


ans=0
for a1,a2 in last.items():
    if a2>=2:
        now=(a2*(a2-1))//2
        ans+=(now)
print(ans)