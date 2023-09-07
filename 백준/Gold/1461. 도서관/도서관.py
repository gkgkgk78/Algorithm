import sys

input = sys.stdin.readline

n, m = map(int, input().split())
minus = []
plus = []
e = list(map(int, input().split()))
mm = -sys.maxsize
for i in e:

    if i < 0:
        minus.append(i)
    elif i > 0:
        plus.append(i)
    mm = max(mm, abs(i))
minus.sort(reverse=True)
plus.sort()
# 이제 시작을 해서 진행을 해보도록 하자

ans = 0
index = m - 1
nex = len(plus)
if len(plus) % m != 0:
    index += len(plus) % m
    if n > 1:
        ans += plus[len(plus) % m - 1] * 2
    else:
        ans += plus[len(plus) % m - 1]
    nex -= 1
for i in range(nex // m):
    ans += plus[index] * 2
    index += m

index = m - 1
nex = len(minus)
if len(minus) % m != 0:

    if n > 1:
        ans += abs(minus[len(minus) % m - 1]) * 2
    else:
        ans += abs(minus[len(minus) % m - 1])
    nex -= 1
    index += len(minus) % m

for i in range(nex // m):
    ans += abs(minus[index]) * 2
    index += m

if n > 1:
    print(ans - mm)
else:
    print(ans)