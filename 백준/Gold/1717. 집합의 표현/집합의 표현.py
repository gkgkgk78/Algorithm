import sys
sys.setrecursionlimit(10**9)
a,b=map(int,sys.stdin.readline().split())
maps=[0]*(a+1)
for i in range(1,a+1):
    maps[i]=i

def find(a):
    if a==maps[a]:
        return a
    b=find(maps[a])
    maps[a]=b
    return b
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    if a<b:
        maps[b]=a
    else:
        maps[a]=b

for i in range(b):
    a1,a2,a3=map(int,sys.stdin.readline().split())

    if a2==7 and a1==1:
        jk=34
    if a1==0:#union
        union(a2,a3)
    else:#같은 집합인지 확인
        if find(a2)==find(a3):
            print("YES")
        else:
            print("NO")





