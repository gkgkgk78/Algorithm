import sys
from collections import deque

input = sys.stdin.readline

graph = []
for _ in range(5):
    e = list(map(str, input().rstrip()))
    graph.append(e)

# 소문난 칠공주를 결성할 수 있는 모든 경우의 수를 출력 하자

total = []
for i in range(5):
    for j in range(5):
        total.append((i, j))
isSelected = [0] * (7)

answer = 0


def game():
    global answer
    q = deque()
    visit = [[0] * (5) for _ in range(5)]
    sx, sy = total[isSelected[0]]
    for i in isSelected:
        x, y = total[i]
        visit[x][y]=1
    q.append((sx,sy))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    co=1
    visit[sx][sy]=2
    while q:
        x, y = q.popleft()
        for i in range(4):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < 5 and 0 <= zy < 5 and visit[zx][zy] == 1:
                visit[zx][zy] = 2
                q.append((zx, zy))
                co+=1


    if co == 7:
        answer += 1


def comb(index, count):
    if count == 7:
        # print(isSelected)
        co=0
        for i in isSelected:
            x, y = total[i]
            if graph[x][y] == "S":
                co += 1
        if co>=4:
            game()
        return
    for i in range(index, 25):
        isSelected[count] = i
        comb(i + 1, count + 1)


comb(0, 0)
print(answer)