import sys


input = sys.stdin.readline
n=int(input().rstrip())
e=[]
for _ in range(n):
    e.append(float(input().rstrip()))
e.sort()

for i in range(7):
    print("{:.3f}".format(e[i]))