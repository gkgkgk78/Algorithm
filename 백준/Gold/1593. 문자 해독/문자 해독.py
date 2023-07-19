import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
e = list(map(str, input().rstrip()))
w = list(map(str, input().rstrip()))

ori1 = Counter(e)
ori = dict(ori1)
find = 0
for a1, a2 in ori.items():
    find += a2
start = 0
fin = n - 1
now = 0
right = dict()

for i in range(n):
    if w[i] in ori:
        now += 1
    if w[i] not in right:
        right[w[i]] = 0
    right[w[i]] += 1

ans = 0
while fin < m:
    t1 = 0
    # 우선 확인을 한다.
    if now == find:
        for a1, a2 in ori.items():
            if a1 not in right or a2 != right[a1]:
                t1 = 1
                break
        if t1 == 0:
            ans += 1

    fin += 1
    if fin == m:
        break
    if w[fin] in ori:
        now += 1
        if w[fin] not in right:
            right[w[fin]] = 0
        right[w[fin]] += 1
    if w[start] in ori:
        now -= 1
        right[w[start]] -= 1
    start += 1

print(ans)