import sys
from collections import deque

input = sys.stdin.readline

ans = "123456780"
visit = dict()

total = []
zy = 0
for i in range(3):
    for j in range(3):
        total.append((i, j))

def find(e):
    for i in range(9):
        if e[i] == "0":
            return i

total1 = [[0] * (3) for _ in range(3)]
tt = 0
for i in range(3):
    for j in range(3):
        total1[i][j] = tt
        tt += 1

def bfs(now):
    q = deque()
    visit[now] = 0
    q.append((now, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        stt, cou = q.popleft()
        if stt == ans:
            return cou
        a1 = find(stt)
        x, y = total[a1]  # 찾아낸 좌표를 의미함

        for i in range(4):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < 3 and 0 <= zy < 3:
                t1 = total1[zx][zy]  # 바꿔낸 위치를 의미를 함
                # 이제 문자열 바꿔서 만들어야 함
                temp = ""
                for i1 in stt:
                    temp += i1
                temp = list(temp)
                temp[t1] = stt[a1]
                temp[a1] = stt[t1]
                e1 = ''.join(temp)
                if e1 not in visit:
                    visit[e1] = cou + 1
                    q.append((e1, cou + 1))
    return -1


graph = []
now = ""
for i in range(3):
    e = list(map(str, input().split()))
    graph.append(e)
    for j in e:
        now += j
if now == ans:
    print(0)
else:
    print(bfs(now))