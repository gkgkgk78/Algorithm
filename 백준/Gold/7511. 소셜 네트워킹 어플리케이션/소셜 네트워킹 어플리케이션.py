import sys

input = sys.stdin.readline

t=int(input().rstrip())


def find(a,parents):
    if parents[a]==a:
        return a
    parents[a]=find(parents[a],parents)
    return parents[a]

def union(a,b,parents):
    a1=find(a,parents)
    a2=find(b,parents)
    if a1<a2:
        parents[a2]=a1
    else:
        parents[a1]=a2


for i in range(1,t+1):
    n=int(input().rstrip())
    parents=[0]*(n+1)

    for k in range(n+1):
        parents[k]=k
    friends=[]
    aa=int(input().rstrip())
    for _ in range(aa):
        a1,a2=map(int,input().split())
        union(a1,a2,parents)
    aa = int(input().rstrip())
    cnt=0
    for k in range(n+1):
        parents[k]=find(k,parents)
    print("Scenario "+(str)(i)+":")
    for _ in range(aa):
        a1,a2=map(int,input().split())
        z1=find(a1,parents)
        z2=find(a2,parents)
        if z1==z2:
            print(1)
        else:
            print(0)
    print()