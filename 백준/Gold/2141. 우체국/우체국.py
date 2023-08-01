import sys

input = sys.stdin.readline
sumz=0
e=[]
n=int(input().rstrip())
for _ in range(n):
    a1,a2=map(int,input().split())
    sumz+=a2
    e.append((a1,a2))
e=sorted(e,key=lambda x:x[0])
if sumz%2==0:
    sumz=sumz//2
else:
    sumz=(sumz//2)+1
ne=0
for a1,a2 in e:
    ne+=a2
    if ne>=sumz:
        print(a1)
        break