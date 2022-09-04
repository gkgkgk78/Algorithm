import sys
input=sys.stdin.readline
a=int(input().rstrip())


def find(a):
    if parent[a]==a:
        return a
    b=find(parent[a])
    parent[a]=b
    return b


def union(a,b):
    a=find(a)
    b=find(b)

    if a==b:
        return
    else:
        parent[b]=a
        number[a]+=number[b]



for i in range(a):
    b=int(input().rstrip())
    parent=dict()
    number=dict()
    for j in range(b):
        t1,t2=map(str,input().split())
        if t1 not in parent:
            parent[t1]=t1
            number[t1]=1
        if t2 not in parent:
            parent[t2] = t2
            number[t2] = 1
        union(t1,t2)
        print(number[find(t1)])