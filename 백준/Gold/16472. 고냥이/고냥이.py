import sys

input = sys.stdin.readline

n = int(input().rstrip())
e = list(map(str, input().rstrip()))

ans = -sys.maxsize
left = 0
right = n - 1
total = dict()
for k in range(right + 1):
    if e[k] not in total:
        total[e[k]] = 1
    else:
        total[e[k]] += 1

if len(total) <= n:
    ans = max(ans, right + 1)
leng = n
while right + 1 < len(e):

    if len(total) <= n:
        right += 1
        if e[right] not in total:
            total[e[right]] = 1
        else:
            total[e[right]] += 1
    else:
        total[e[left]] -= 1
        if total[e[left]] == 0:
            total.pop(e[left])
        left += 1

    if len(total) <= n:
        ans = max(ans, right - left + 1)

print(ans)