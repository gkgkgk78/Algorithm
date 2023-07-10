import sys

input = sys.stdin.readline

n = 5
m = 8
t = int(input().rstrip())
gpin = sys.maxsize


def dfs(graph):
    global gpin

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    for i in range(5):
        for j in range(9):
            if graph[i][j] == "o":
                # 이때 왼쪽 오른쪽 위, 아래 탐지하는 로직이 필요함
                for k in range(4):
                    zx = i
                    zy = j
                    zx += dx[k]  # 찾은 핀
                    zy += dy[k]
                    if 0 <= zx < 5 and 0 <= zy < 9:
                        if graph[zx][zy] == "o":
                            tx = zx + dx[k]
                            ty = zy + dy[k]
                            if 0 <= tx < 5 and 0 <= ty < 9:
                                if graph[tx][ty] == ".":
                                    graph[i][j] = "."
                                    graph[zx][zy] = "."
                                    graph[tx][ty] = "o"
                                    dfs(graph)
                                    graph[i][j] = "o"
                                    graph[zx][zy] = "o"
                                    graph[tx][ty] = "."
    cc = 0
    for i in range(5):
        for j in range(9):
            if graph[i][j] == "o":
                cc += 1

    gpin = min(gpin, cc)
 

for a in range(t):
    graph = []
    fin_count = 0
    gpin = sys.maxsize

    for _ in range(n):
        e = list(map(str, input().rstrip()))
        graph.append(e)
        for i in e:
            if i == "o":
                fin_count += 1
    dfs(graph)
    print(gpin, fin_count - gpin)
    if a == t - 1:
        break

    e = input().rstrip()