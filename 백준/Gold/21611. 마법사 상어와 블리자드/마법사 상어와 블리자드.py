#1시간 30분
import sys
from collections import deque

input = sys.stdin.readline

#
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

go = []
for _ in range(m):
    dir, leng = map(int, input().split())
    go.append([dir, leng])

tx, ty = n // 2, n // 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

one = 0
two = 0
third = 0


def read_square():
    x = tx
    y = ty
    temp = 1
    dir = 0
    q = deque()
    while 1:
        for _ in range(2):
            for _ in range(temp):
                x += dx[dir]
                y += dy[dir]
                if graph[x][y] != -1 and graph[x][y] != 0:
                    q.append(graph[x][y])
                if x == 0 and y == 0:
                    return q
            dir = (dir + 1) % 4
        temp += 1


def destroy(dir, leng):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    x = tx
    y = ty
    for _ in range(leng):
        x += dx[dir]
        y += dy[dir]
        graph[x][y] = -1


def print_graph():
    for i in graph:
        print(i)
    print()


def bomb(q):
    global one, two, third
    check = 0
    while 1:
        check = 0
        tempq = deque()
        last = deque()
        go_check = 0
        while q:
            a1 = q.popleft()

            if tempq and tempq[-1] != a1:  # 그전과 다르다면
                if go_check >= 4:  # 그냥 비운다.
                    if tempq[-1] == 1:
                        one += len(tempq)
                    elif tempq[-1] == 2:
                        two += len(tempq)
                    else:
                        third += len(tempq)
                    tempq = deque()
                    check += 1

                else:
                    while tempq:
                        last.append(tempq.popleft())

                go_check = 1
                tempq.append(a1)
            else:
                tempq.append(a1)
                go_check += 1

        if len(tempq) < 4:
            # 마지막으로 한번더 진행 해야함
            while tempq:
                last.append(tempq.popleft())
        else:
            if tempq[-1] == 1:
                one += len(tempq)
            elif tempq[-1] == 2:
                two += len(tempq)
            else:
                third += len(tempq)
        q = last
        if check == 0:
            return q


def make_group(q):
    check = 0
    tempq = deque()
    last = deque()
    go_check = 0
    while q:
        a1 = q.popleft()
        if tempq and tempq[-1] != a1:  # 그전과 다르다면
            last.append(len(tempq))
            last.append(tempq[-1])
            tempq = deque()
            go_check = 1
            tempq.append(a1)
        else:
            tempq.append(a1)
            go_check += 1

    if len(tempq) > 0:
        # 마지막으로 한번더 진행 해야함
        last.append(len(tempq))
        last.append(tempq[-1])

    return last


def last_batch(q):
    x = tx
    y = ty
    temp = 1
    dir = 0
    while 1:
        for _ in range(2):
            for _ in range(temp):
                x += dx[dir]
                y += dy[dir]
                if len(q) > 0:
                    graph[x][y] = q.popleft()
                else:
                    graph[x][y] = -1
                if x == 0 and y == 0:
                    return
            dir = (dir + 1) % 4

        temp += 1


for i in range(m):
    dir, leng = go[i]
    # 파괴
    destroy(dir, leng)

    # 다읽고 큐에 넣음
    q = read_square()

    # 폭발
    q = bomb(q)

    # 구슬 변화 과정
    q = make_group(q)
    last_batch(q)

print(one + two * 2 + third * 3)