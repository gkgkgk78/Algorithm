import sys

input = sys.stdin.readline
n = int(input().rstrip())
e = []
for i in range(n):
    a1, a2, a3, a4 = map(str, input().split())
    a2 = (int)(a2)
    a3 = (int)(a3)
    a4 = (int)(a4)
    e.append([a1,a2,a3,a4])
e=sorted(e,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in e:
    print(i[0])