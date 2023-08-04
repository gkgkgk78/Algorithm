import sys

input = sys.stdin.readline
n, k = map(int, input().split())
e = list(map(int, input().split()))

find = dict()
find[e[0]] = 1
ans = 0
if e[0] == k:
    ans += 1

for l in range(1, n):
    e[l] += e[l - 1]
    next = e[l] - k
    if next in find:
        ans += find[next]
    if e[l] not in find:
        find[e[l]] = 1
    else:
        find[e[l]] += 1
    if e[l] == k:
        ans += 1

print(ans)