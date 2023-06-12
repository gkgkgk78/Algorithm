import sys

input = sys.stdin.readline
n=int(input().rstrip())
e = list(map(int, input().split()))
a2=list(map(int,input().split()))

for l in range(n):
    e[l]-=a2[l]

find = dict()
find[e[0]] = 1
ans = 0
if e[0] == 0:
    ans += 1
for l in range(1, n):
    e[l] += e[l - 1]
    next = e[l]
    if next in find:
        ans += find[next]
    if next not in find:
        find[next] = 1
    else:
        find[next] += 1
    if e[l] == 0:
        ans += 1

print(ans)