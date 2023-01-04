import sys


input = sys.stdin.readline

graph = []
one = []
color = [0, 5, 5, 5, 5, 5]  # 색종이 개수를 의미를 함
answer = sys.maxsize
for i in range(10):
    e = list(map(int, input().split()))
    graph.append(e)
    for j in range(10):
        if e[j] == 1:
            one.append((i, j))


def findmax(x, y):
    find = 1
    for l in range(2, 6):
        if x + l > 10 or y + l > 10:
            break
        for i in range(x, x + l):
            for j in range(y, y + l):
                if graph[i][j] == 0:
                    return find
        find += 1
    return find


def dfs(tx,ty,graph, color, depth):
    global answer
    # 이제 파악을 하도록 해야함

    if tx==9 and ty>9:

        answer=min(answer,depth)
        return

    if depth >= answer:
        return

    if ty > 9:
        dfs(tx + 1, 0, graph, color, depth)
        return


    if graph[tx][ty] == 1:
            # 역순으로 수를 체크를 하면서 모든 경우의 수를 다 확인을 해보도록 하자
            u = findmax(tx, ty)
            for k in range(u, 0, -1):
                if color[k] > 0:
                    color[k] -= 1
                    for i in range(tx, tx + k):
                        for j in range(ty, ty + k):
                            graph[i][j] = 0
                    dfs(tx,ty+1,graph, color, depth + 1)
                    for i in range(tx, tx + k):
                        for j in range(ty, ty + k):
                            graph[i][j] = 1
                    color[k] += 1
    else :
        dfs(tx,ty+1,graph, color,depth)

if len(one) == 0:
    print(0)
else:
    dfs(0,0,graph, color, 0)  # x,y,전체 그래프, 색종이 개수

    if answer == sys.maxsize:
        print(-1)
    else:
        print(answer)