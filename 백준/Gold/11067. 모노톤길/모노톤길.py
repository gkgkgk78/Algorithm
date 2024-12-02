import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    e = []
    for _ in range(n):
        a1, a2 = map(int, input().split())
        e.append((a1, a2))
    e = sorted(e, key=lambda x: (x[0], x[1]))
    graph = dict()
    for a1, a2 in e:
        if a1 not in graph:
            graph[a1] = []
        graph[a1].append(a2)
    answer = []
    x, y = 0, 0
    for key in graph.keys():
        zx = key
        zy = graph[key]
        fy = zy[0]
        ly = zy[-1]
        first = abs(y - fy) + abs(zx - x)
        second = abs(y - ly) + abs(zx - x)
        if first > second:
            zy.reverse()
        for i in zy:
            answer.append((zx, i))
            y = i
        x = zx
    last = list(map(int, input().split()))
    for i in range(1, len(last)):
        a1, a2 = answer[last[i] - 1]
        print((str)(a1) + " " + (str)(a2))