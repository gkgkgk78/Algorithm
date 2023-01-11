
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
e=list(map(int,input().split()))

false=dict()
parents=[0]*(n+1)
def make():
    for i in range(1,n+1):
        parents[i]=i
def find(a):

    if parents[a]==a:
        return a

    parents[a]=find(parents[a])
    return parents[a]

def union(a,b):
    t1=find(a)
    t2=find(b)

    if t1 in false:
        parents[t2]=t1
        return 1
    if t2 in false:
        parents[t1]=t2
        return 1
    if t1<t2:
        parents[t2]=t1
    else:
        parents[t1]=t2
    return 0

make()
for k in range(1,len(e)):
        false[e[k]]=1
total=[]

for i in range(m):
        temp=list(map(int,input().split()))
        total.append(temp[1:])
        for j in range(1,len(temp)-1):
            a1=temp[j]
            a2=temp[j+1]
            union(a1,a2)

answer=0
for i in total:
    t2=0
    for l in i:
        if find(l) in false:
            t2=1
            break
    if t2==0:
            answer+=1
print(answer)