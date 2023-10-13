import sys
input = sys.stdin.readline

dir = dict()
dir[1] = [[[0, 1]], [[1, 0]], [[-1, 0]], [[0, -1]]]
dir[2] = [ [[0, 1], [0, -1]], [[-1, 0], [1, 0]] ]
dir[3] = [ [[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]]
dir[4] = [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]]]
dir[5] = [ [[0, -1], [-1, 0], [0, 1], [1, 0]]]

ans = sys.maxsize
cctv = []
graph = []
n, m = map(int, input().split())
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if 1 <= e[j] <= 5:
            cctv.append((i, j))
    graph.append(e)


def paint(index, dirz, temp):
    x, y = cctv[index]
    ee = dir[graph[x][y]]

    for a1, a2 in ee[dirz]:
        zx = x
        zy = y
        while 1:
            zx += a1
            zy += a2
            if 0 <= zx < n and 0 <= zy < m:
                if graph[zx][zy] == 6:
                    break
                if 1 <= graph[zx][zy] <= 5:
                    continue
                temp[zx][zy] = -1
            else:
                break


def game(now):
    global ans
    temp = [[0] * (m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]

    # 이제 cctv 방향 대로 따라서 만들면 된다
    cc = 0
    for i in now:
        paint(cc, i, temp)
        cc += 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    ans = min(ans, cnt)


def dfs(now, index):
    if len(now) == len(cctv):
        game(now)
        return
    x, y = cctv[index]
    aa = dir[graph[x][y]]
    for i in range(len(aa)):
        now.append(i)
        dfs(now, index + 1)
        now.pop()


dfs([], 0)
print(ans)