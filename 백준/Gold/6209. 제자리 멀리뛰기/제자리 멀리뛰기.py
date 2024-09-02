import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
temp = []
for _ in range(n):
    e = (int)(input().rstrip())
    temp.append(e)
temp.sort()

left = 0
right = d + 1


def bi(mid):
    before = 0
    count = 0
    for i in range(len(temp)):
        now = temp[i] - before
        if now >= mid:
            before = temp[i]
        else:
            count += 1
    return count


answer = -1
while left + 1 < right:
    mid = (left + right) // 2
    check = bi(mid)
    if check <= m:
        left = mid
        answer = mid
    else:
        right = mid
print(answer)