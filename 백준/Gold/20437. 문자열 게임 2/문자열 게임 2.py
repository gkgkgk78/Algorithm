import sys

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):

    e = list(map(str, input().rstrip()))
    k = int(input().rstrip())
    first = dict()
    for l in  range(len(e)):
        if e[l] in first:
            first[e[l]].append(l)
        else:
            first[e[l]] = [l]
    avail = []
    for a1, a2 in first.items():
        if len(a2) >= k:
            avail.append(a1)

    if len(avail) == 0:
        print(-1)
        continue

    # 이제 각 문자당 해서 한번 시작을 해 보도록 하자
    third = sys.maxsize
    fourth = -sys.maxsize

    for now in avail:

        count = 0
        left = 0
        right = k-1
        temp=first[now]

        while right < len(temp):
            third = min(third, temp[right] - temp[left] + 1)
            fourth = max(fourth,  temp[right] - temp[left] + 1)
            right+=1
            left+=1

    print(third,fourth)