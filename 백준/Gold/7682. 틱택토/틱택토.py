import sys

input = sys.stdin.readline


def check(graph, find):
    # 가로
    if graph[0][0] == find and graph[0][1] == find and graph[0][2] == find:
        return 1

    if graph[1][0] == find and graph[1][1] == find and graph[1][2] == find:
        return 1
    if graph[2][0] == find and graph[2][1] == find and graph[2][2] == find:
        return 1
    # 세로
    if graph[0][0] == find and graph[1][0] == find and graph[2][0] == find:
        return 1
    if graph[0][1] == find and graph[1][1] == find and graph[2][1] == find:
        return 1
    if graph[0][2] == find and graph[1][2] == find and graph[2][2] == find:
        return 1
    # 대각선
    if graph[0][0] == find and graph[1][1] == find and graph[2][2] == find:
        return 1

    if graph[2][0] == find and graph[1][1] == find and graph[0][2] == find:
        return 1

    return 0


while 1:
    e = list(map(str, input().rstrip()))
    nn = ''.join(e)
    if nn == "end":
        break
    graph = []
    c = 0
    counto = 0
    countx = 0
    countzero = 0
    for i in e:
        if i == "X":
            countx += 1
        elif i == "O":
            counto += 1
        else:
            countzero += 1

    graph.append(e[:3])
    graph.append(e[3:6])
    graph.append(e[6:])
    z1 = check(graph, "X")
    z2 = check(graph, "O")

    if z1 == 1 and z2 == 1:
        print("invalid")
        continue

    if counto + 1 == countx:
        if z1 == 1:
            print("valid")
            continue
    elif counto == countx:
        if z2 == 1:
            print("valid")
            continue

    if countzero == 0 and countx == 5 and counto == 4 and z1==0 and z2==0:
        print("valid")
        continue
    print("invalid")