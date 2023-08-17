import sys
input = sys.stdin.readline

n=int(input().rstrip())

e=dict()
for _ in range(n):
    a1,a2=map(int,input().split())
    if a1 not in e:
        e[a1]=0
    if a2 not in e:
        e[a2]=0
    e[a1]+=1
    e[a2]-=1

g=sorted(e.keys())

sumz=0
now=[0,0]
check=0
temp=0
for i in g:
    temp+=e[i]
    if temp>sumz:
        sumz=temp
        check=1
        now[0]=i
    if temp<sumz and check:
        check=0
        now[1]=i
print(sumz)
print(now[0],now[1])