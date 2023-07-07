import sys

input = sys.stdin.readline

n = int(input().rstrip())
e = []
for i in range(n):
    now = str(input().rstrip())
    e.append((now, i))
e.sort()

total = dict()

count = -sys.maxsize
count_str = ""
count_idx=-1
for i in range(1, n):

    st, co = e[i]
    # 체크 해보는 단계 시작
    before = e[i - 1][0]
    before_idx = e[i - 1][1]
    if st == before:
        continue
    left = min(len(before), len(st))
    next_idx=min(co,before_idx)
    t = 0
    next = ""
    while t < left:
        if before[t] != st[t]:
            break
        next += before[t]
        t += 1

    if next not in total:
        total[next] = []
        total[next].append([before, before_idx])
    total[next].append([st, co])

    if len(next) > len(count_str):
        count_str = next
        count_idx=next_idx
    elif len(next)==len(count_str):
        if next_idx<count_idx:
            count_str = next
            count_idx = next_idx

a = total[count_str]
a = sorted(a, key=lambda x: x[1])

for i in range(2):
    print(a[i][0])