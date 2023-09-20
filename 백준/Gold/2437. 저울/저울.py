import sys

input = sys.stdin.readline
n=int(input().rstrip())
e=list(map(int,input().split()))
e.sort()
now=1
for i in e:
    if now<i:
        break
    now+=i
print(now)