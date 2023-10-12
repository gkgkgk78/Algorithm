import sys

input = sys.stdin.readline

n = int(input().rstrip())
e = list(map(int, input().split()))
left = 0
right = 0
total = dict()
total[e[right]] = 1
ans = 0
while 1:

    if total[e[right]] == 1:
        ans += (right - left + 1)
    else:
        while 1:
            total[e[left]]-=1
            left+=1
            if total[e[left]]==1 and total[e[right]]==1:
                ans += (right - left + 1)
                break
    right += 1
    if right == n:
        break
    if e[right] not in total:
        total[e[right]] = 0
    total[e[right]] += 1

print(ans)