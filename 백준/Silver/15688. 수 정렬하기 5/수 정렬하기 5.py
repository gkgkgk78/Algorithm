import sys

input = sys.stdin.readline

n=int(input().rstrip())
e=[]
for _ in range(n):
    e.append(int(input().rstrip()))
e.sort()
for i in e:
    print(i)