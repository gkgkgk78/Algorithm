import sys

input = sys.stdin.readline

e = list(map(str, input().rstrip()))

cou = 0
for i in e:
    if i == "a":
        cou += 1
left = 0
right = cou - 1
coua = 0
coub = 0
for i in range(left, right + 1):
    if e[i] == "a":
        coua += 1
    else:
        coub += 1

ans = sys.maxsize
for _ in range(len(e)):

    # 이제 체크 한번 하는 거임
    ans = min(ans, coub)
    right += 1
    if right == len(e):
        right = 0
    if e[right] == "b":
        coub += 1
    if e[left] == "b":
        coub -= 1
    left += 1
print(ans)