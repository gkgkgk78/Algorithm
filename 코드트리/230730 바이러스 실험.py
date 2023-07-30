import sys

input = sys.stdin.readline

n, m, k1 = map(int, input().split())

graph = [[5] * (n) for _ in range(n)]
add_growth = []
for _ in range(n):
    add_growth.append(list(map(int, input().split())))

now_virus = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    now_virus[a1 - 1][a2 - 1].append(a3)


def up_virus(next_virus, up_five, death_virus):
    for i in range(n):
        for j in range(n):
            if len(now_virus[i][j]) > 0:
                # 이제 시작 해야함
                a1 = now_virus[i][j]
                a1.sort()
                for k in a1:
                    if graph[i][j] - k >= 0:
                        graph[i][j] -= k
                        next_virus.append((i, j, k + 1))
                        if (k + 1) % 5 == 0:
                            up_five.append((i, j))
                    else:
                        death_virus.append((i, j, k))
                now_virus[i][j] = []


def go(next_virus):
    for a1, a2, a3 in next_virus:
        now_virus[a1][a2].append(a3)


def up(death_virus):
    for a1, a2, a3 in death_virus:
        graph[a1][a2] += (a3 // 2)


def move(up_five):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for a1, a2 in up_five:
        g1 = now_virus
        for i in range(8):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < n and 0 <= zy < n:
                now_virus[zx][zy].append(1)


def gogo():
    for i in range(n):
        for j in range(n):
            graph[i][j] += add_growth[i][j]


for kk in range(k1):
    # 바이러스 양분 섭취 시작 하기
    next_virus = []
    up_five = []
    death_virus = []
    up_virus(next_virus, up_five, death_virus)
    # 바이러스 원래대로 맞추기
    go(next_virus)

    # 죽은 바이러스 증가
    up(death_virus)

    # 번식 진행
    if len(up_five) > 0:
        move(up_five)

    # 양분 추가
    gogo()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(now_virus[i][j])
print(ans)