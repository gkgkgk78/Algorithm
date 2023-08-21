#우선순위큐 다중조건 정렬 몰라서 시간 걸렸고
#제대로 구현 되었다고 생각한 부분을 고려 못해서 시간 걸림..

import sys
import heapq

input = sys.stdin.readline

q = int(input())
total1 = 0


def end():
    tt = -sys.maxsize
    for i1, a2 in rabbit_total.items():
        if a2[3] > tt:
            tt = a2[3]

    return tt + total1


def find(x, y, dis):
    # 동3 서1 남2 북0 방향으로 이동 시켜 보도록 하자

    temp = []
    for i in range(4):

        zx = x
        zy = y
        if i == 3:  # 동
            next = dis
            next %= ((m - 1) * 2)
            if zy + next <= m:
                temp.append((zx, zy + next))
            else:
                # 오 왼 오 할거임
                first = m - zy
                zy = m
                next -= first
                if zy - next >= 1:
                    temp.append((zx, zy - next))
                else:
                    next -= (zy - 1)
                    zy = 1
                    # 오
                    zy += next
                    temp.append((zx, zy))

        elif i == 1:  # 서
            next = dis
            next %= ((m - 1) * 2)
            if zy - next >= 1:
                temp.append((zx, zy - next))
            else:
                # 왼 오 왼 할거임
                first = zy - 1
                zy = 1
                next -= first
                if zy + next <= m:  # 오
                    temp.append((zx, zy + next))
                else:
                    next -= (m - zy)
                    zy = m
                    # 왼
                    zy -= next
                    temp.append((zx, zy))


        elif i == 2:  # 북
            next = dis
            next %= ((n - 1) * 2)
            if zx - next >= 1:  # 위
                temp.append((zx - next, zy))
            else:
                first = zx - 1
                zx = 1
                next -= first
                if zx + next <= n:  # 아래
                    temp.append((zx + next, zy))
                else:

                    next -= (n - zx)
                    zx = n
                    # 위
                    zx -= next
                    temp.append((zx, zy))

        elif i == 0:  # 남
            next = dis
            next %= ((n - 1) * 2)
            if zx + next <= n:  # 아래
                temp.append((zx + next, zy))
            else:
                first = n - zx
                zx = n
                next -= first
                if zx - next >= 1:  # 위
                    temp.append((zx - next, zy))
                else:
                    next -= (zx - 1)
                    zx = 1
                    # 아래
                    zx += next
                    temp.append((zx, zy))

    # 이제 우선 순위를 정해보도록 하자
    temp = sorted(temp, key=lambda x: (-(x[0] + x[1]), -x[0], -x[1]))

    return (temp[0][0], temp[0][1])


# 0:pid 1:거리 2:지금까지 횟수 3:점수 4:x 5:y
def move(k, s,ee):
    # 가장 우선 순위 높은 토끼를 뽑아보자
    score = dict()
    rabbit = []
    global total1
    for i1, a2 in rabbit_total.items():
        pid, dis, count, sco, x, y = a2
        temp = [count, x + y, x, y, pid]  # 점프횟수, 행+열, 행번호작은, 열번호작은, 고유번호
        heapq.heappush(rabbit, temp)
    if ee==16:
        ee=1
    for _ in range(k):
        tt = heapq.heappop(rabbit)  # 이제 한명의 토끼가 나옴

        now = tt[4]
        now1 = rabbit_total[now]

        # 우선 순위가 가장 높은 토끼가 정해짐
        # 이제 해당 되는 토끼를 이동 시켜 보도록 하자
        a1, a2 = find(now1[4], now1[5], now1[1])

        # 이제 토끼 이동 해주면 됨
        total1 += (a1 + a2)
        if now not in score:
            score[now] = [-1, -1]
        e1 = rabbit_total[now]
        e1[4] = a1
        e1[5] = a2
        e1[2] = tt[0] + 1
        e1[3] -= (a1 + a2)
        # 0:pid 1:거리 2:지금까지 횟수 3:점수 4:x 5:y
        # 0:점프횟수, 1:행+열, 2:행번호작은, 3:열번호작은, 4:고유번호
        rabbit_total[now] = e1
        score[now] = [a1, a2]
        # 점프횟수, 행+열, 행번호작은, 열번호작은, 고유번호
        ne = [tt[0] + 1, a1 + a2, a1, a2, tt[4]]

        heapq.heappush(rabbit, ne)

    # 이제 s만큼 더해 줘야함
    # dict에서 판단을 해서 우선순위를 두어 가장 우선 순위가 높은 토끼를 구해보도록 하자
    total = []
    for a1, a2 in score.items():
        x1, y1 = a2
        total.append((a1, x1, y1))

    total = sorted(total, key=lambda x: (-(x[1] + x[2]), -x[1], -x[2], -x[0]))
    check = total[0][0]
    nn = rabbit_total[check]
    nn[3] += s
    rabbit_total[check] = nn


rabbit_total = dict()

n = -1
m = -1
for oo in range(q):

    e = list(map(int, input().split()))
    if e[0] == 100:
        n = e[1]
        m = e[2]
        index = 4
        while index < len(e):
            rabbit_total[e[index]] = [e[index], e[index + 1], 0, 0, 1, 1]
            index += 2
    elif e[0] == 200:
        move(e[1], e[2],oo)
    elif e[0] == 300:
        aa = rabbit_total[e[1]]
        aa[1] *= e[2]
        rabbit_total[e[1]] = aa

    else:
        aa = end()
        print(aa)